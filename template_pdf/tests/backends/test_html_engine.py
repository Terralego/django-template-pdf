from django.template import Template
from django.test import TestCase

from template_pdf.backends.html import HtmlEngine, HtmlTemplate
from template_pdf.tests.backends.backend_settings import (
    HERE, HTML_TEMPLATE_PATH, RENDERED_CONTENT_HTML_TEMPLATE_SCREENSHOT)


class TestHtmlEngine(TestCase):

    def setUp(self):
        self.params = {
            'NAME': 'html',
            'DIRS': [HERE],
            'APP_DIRS': True,
            'OPTIONS': [],
        }
        self.html_engine = HtmlEngine(self.params)

    def test_get_template_content_works(self):
        content = self.html_engine.get_template_content(HTML_TEMPLATE_PATH)
        self.assertIsInstance(content, str)
        with open(HTML_TEMPLATE_PATH, 'r') as read_file:
            self.assertEqual(content, read_file.read())

    def test_get_template_works(self):
        template = self.html_engine.get_template('template.html')
        self.assertIsInstance(template, HtmlTemplate)
        self.assertIsInstance(template.template, Template)

    def test_render_works(self):
        class Obj:
            name = 'Michel'
        template = self.html_engine.get_template('template.html')
        rendered = template.render(context={'object': Obj()})
        self.assertIsInstance(rendered, str)
        with open(RENDERED_CONTENT_HTML_TEMPLATE_SCREENSHOT, 'r') as read_file:
            self.assertEqual(read_file.read(), rendered)
