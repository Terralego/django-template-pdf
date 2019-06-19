from django.conf import settings
from django.template.response import TemplateResponse

from template_pdf.pdf_convertor.client import to_pdf


class ToPdfResponse(TemplateResponse):

    @property
    def rendered_content(self):
        content = super().rendered_content
        pdf_convertor_host = getattr(settings, 'PDF_CONVERTOR_HOST', 'localhost')
        pdf_convertor_port = getattr(settings, 'PDF_CONVERTOR_PORT', 9999)
        return to_pdf(pdf_convertor_host, pdf_convertor_port, content)
