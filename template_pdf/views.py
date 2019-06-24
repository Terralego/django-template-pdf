from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.views.generic.detail import BaseDetailView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from template_pdf.mixins import (AbstractTemplateResponseMixin,
                                 SingleObjectMixin)
from template_pdf.models import DocumentTemplate
from template_pdf.responses import HtmlToPdfResponse, OdtToPdfResponse
from template_pdf.serializers import DocumentTemplateSerializer

MAPPING_RESPONSE_CLASS = {
    'odt': OdtToPdfResponse,
    'html': HtmlToPdfResponse,
}


class AbstractHtmlTemplateToPdfView(AbstractTemplateResponseMixin, SingleObjectMixin,
                                    BaseDetailView):
    """
    This view handles GET requests. It fills the html template associated with a given object with
    its fields. It can not be used alone. You must implement your own view specifying at least a
    `queryset` or a `model`.

    You can also specify a `field` to use to find the object. This must however be a primary key.
    If so, you need to specify the `field_url_kwarg` used in the url. By default the `pk` is used.
    """
    template_name_suffix = '.html'
    response_class = HtmlToPdfResponse
    content_type = 'application/pdf'


class AbstractOdtTemplateToPdf(AbstractTemplateResponseMixin, SingleObjectMixin, BaseDetailView):
    """
    This view handles GET requests. It fills the odt template associated with a given object with
    its fields. It can not be used alone. You must implement your own view specifying at least a
    `queryset` or a `model`.

    You can also specify a `field` to use to find the object. This must however be a primary key.
    If so, you need to specify the `field_url_kwarg` used in the url. By default the `pk` is used.

    Moreover, a convertor server is needed. If you decide not to run it on localhost
    PDF_CONVERTOR_HOST and PDF_CONVERTOR_PORT must be specified in the settings.
    """
    template_name_suffix = '.odt'
    response_class = OdtToPdfResponse
    content_type = 'application/pdf'


class DocumentTemplateViewSet(ModelViewSet, SingleObjectMixin):
    queryset = DocumentTemplate.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = DocumentTemplateSerializer

    content_type = 'application/pdf'

    def render_to_response(self, response_class, request, template_path, context, template_engine,
                           **response_kwargs):
        """
        Return a response, using the `response_class` for this view, with a
        template rendered with the given context.

        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault('content_type', self.content_type)
        return response_class(
            request=request,
            template=template_path,
            context=context,
            using=template_engine,
            **response_kwargs
        )

    @action(detail=False, methods=['get'],
            url_path='(?P<app_label>[^/]+)/(?P<model_name>[^/]+)')
    def list_by_object(self, request, app_label=None, model_name=None):
        model_class = apps.get_model(app_label, model_name=model_name)
        content_type = ContentType.objects.get_for_model(model_class)
        templates = (
            DocumentTemplate.objects
            .filter(content_type=content_type)
            .all()
        )
        templates = [self.serializer_class(e).data for e in templates]
        return Response(data=templates)

    @action(detail=True, methods=['get'],
            url_path='(?P<app_label>[^/]+)/(?P<model_name>[^/]+)/(?P<object_id>[0-9]+)')
    def fill_template(self, request, app_label=None, model_name=None, object_id=None):
        template = self.get_object()
        model_class = apps.get_model(app_label, model_name=model_name)
        obj = get_object_or_404(model_class, pk=object_id)
        context = self.get_context_data(object=obj)
        return self.render_to_response(MAPPING_RESPONSE_CLASS[template.format], request,
                                       template.documenttemplate.url, context, template.format)
