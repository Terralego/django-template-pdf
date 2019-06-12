from django.views.generic.detail import BaseDetailView

from template_pdf.mixins import (AbstractTemplateResponseMixin,
                                 SingleObjectMixin)
from template_pdf.responses import HtmlToPdfResponse


class AbstractHtmlTemplateToPdfView(AbstractTemplateResponseMixin, SingleObjectMixin,
                                    BaseDetailView):
    """
    This view handles GET requests. It fills the template associated with a given object with its
    fields. It can not be used alone. You must implement your own view specifying at least a
    `queryset` or a `model`.

    You can also specify a `field` to use to find the object. This must however be a primary key.
    If so, you need to specify the `field_url_kwarg` used in the url.
    """
    template_name_suffix = '.html'
    response_class = HtmlToPdfResponse
    content_type = 'application/pdf'
