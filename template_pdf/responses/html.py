from django.template.response import TemplateResponse

from weasyprint import HTML


class HtmlToPdfResponse(TemplateResponse):

    @property
    def rendered_content(self):
        content = super().rendered_content
        return HTML(string=content).write_pdf()
