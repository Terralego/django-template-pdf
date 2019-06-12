from io import BytesIO
from zipfile import ZipFile

from django.template import Template
from django.template.exceptions import TemplateDoesNotExist
from django.test import TestCase

from template_pdf.backends.odt import OdtEngine, OdtTemplate
from template_pdf.tests.backends.backend_settings import (
    CONTENT_SCREENSHOT_PATH, HERE, ODT_TEMPLATE_PATH,
    RENDERED_CONTENT_SCREENSHOT)


class TestOdtEngine(TestCase):

    def setUp(self):
        self.params = {
            'NAME': 'odt',
            'DIRS': [HERE],
            'APP_DIRS': True,
            'OPTIONS': [],
        }
        self.odt_engine = OdtEngine(self.params)

    def test_get_template_path_works(self):
        self.assertEqual(self.odt_engine.get_template_path('template.odt'), ODT_TEMPLATE_PATH)
        params2 = {
            'NAME': 'odt',
            'DIRS': ['/bad/path', HERE],
            'APP_DIRS': True,
            'OPTIONS': [],
        }
        odt_engine2 = OdtEngine(params2)
        self.assertEqual(odt_engine2.get_template_path('template.odt'), ODT_TEMPLATE_PATH)
        params3 = {
            'NAME': 'odt',
            'DIRS': [HERE, '/bad/path'],
            'APP_DIRS': True,
            'OPTIONS': [],
        }
        odt_engine3 = OdtEngine(params3)
        self.assertEqual(odt_engine3.get_template_path('template.odt'), ODT_TEMPLATE_PATH)
        params4 = {
            'NAME': 'odt',
            'DIRS': ['/bad/path'],
            'APP_DIRS': True,
            'OPTIONS': [],
        }
        odt_engine4 = OdtEngine(params4)
        with self.assertRaises(TemplateDoesNotExist):
            odt_engine4.get_template_path('template.odt')

    def test_get_template_path_bad_template_name(self):
        with self.assertRaises(TemplateDoesNotExist):
            self.odt_engine.get_template_path('bad_name')

    def test_get_template_content_works(self):
        with open(CONTENT_SCREENSHOT_PATH, 'r') as read_file:
            self.assertEqual(self.odt_engine.get_template_content(ODT_TEMPLATE_PATH),
                             read_file.read())

    def test_get_template_works(self):
        template = self.odt_engine.get_template('template.odt')
        self.assertIsInstance(template, OdtTemplate)
        self.assertIsInstance(template.template, Template)
        self.assertEqual(template.template_path, ODT_TEMPLATE_PATH)

    def test_render(self):
        class Obj:
            name = 'Michel'
        template = self.odt_engine.get_template('template.odt')
        rendered = template.render(context={'object': Obj()})
        self.assertIsInstance(rendered, bytes)
        buffer = BytesIO(rendered)
        with ZipFile(buffer, 'r') as zip_read_file:
            with open(RENDERED_CONTENT_SCREENSHOT, 'r') as read_file:
                self.assertEqual(zip_read_file.read('content.xml').decode(), read_file.read())
