from django.views.generic.detail import BaseDetailView

from template_pdf.mixins import (AbstractTemplateResponseMixin,
                                 SingleObjectMixin)
from template_pdf.responses import ToPdfResponse


class AbstractTemplateToPdfView(AbstractTemplateResponseMixin, SingleObjectMixin,
                                BaseDetailView):
    """
    This view handles GET requests. It fills the template associated with a given object with
    its fields. It can not be used alone. You must implement your own view specifying at least a
    `queryset` or a `model`.

    You can also specify a `field` to use to find the object. This must however be a primary key.
    If so, you need to specify the `field_url_kwarg` used in the url. By default the `pk` is used.

    Moreover, a convertor server is needed. If you decide not to run it on localhost
    PDF_CONVERTOR_HOST and PDF_CONVERTOR_PORT must be specified in the settings.
    """
    response_class = ToPdfResponse
    content_type = 'application/pdf'
