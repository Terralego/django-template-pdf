from django.conf import settings
from django.template import Context
from django.template.context import make_context

from template_pdf.backends.abstract import AbstractEngine


class HtmlTemplate:

    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        context = make_context(context, request)
        return self.template.render(Context(context))


class HtmlEngine(AbstractEngine):
    app_dirname = getattr(settings, 'HTML_ENGINE_APP_DIRNAME', 'html')
    template_class = HtmlTemplate

    def get_template_content(self, template_name):
        template_path = self.get_template_path(template_name)
        with open(template_path, 'r') as read_file:
            return read_file.read()

    def get_template(self, template_name):
        content = self.get_template_content(template_name)
        return self.from_string(content)
