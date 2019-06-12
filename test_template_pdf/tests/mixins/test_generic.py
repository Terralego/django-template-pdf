from unittest.mock import patch

from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase

from template_pdf.mixins import AbstractTemplateResponseMixin


class Meta:
    app_label = 'wow'
    model_name = 'bidon'


class Bidon:
    def __init__(self, name, template_name):
        self.name = name
        self.template_name = template_name
        self._meta = Meta()


class TestGeneric(TestCase):

    def setUp(self):
        self.mixin = AbstractTemplateResponseMixin()
        self.object = Bidon('Michel', 'Pierre')

    def test_get_template_names_with_template_name(self):
        self.mixin.template_name = 'Michel'
        self.assertEqual(self.mixin.get_template_names(), ['Michel'])

    def test_get_template_names_with_template_name_field(self):
        self.mixin.object = self.object
        self.mixin.template_name_field = 'template_name'
        self.assertEqual(['Pierre'], self.mixin.get_template_names())

    @patch('template_pdf.mixins.abstract.isinstance')
    def test_get_template_names_with_object(self, mock_isinstance):
        mock_isinstance.side_effect = lambda *args: True
        self.mixin.template_name_suffix = '.odt'
        self.mixin.object = self.object
        self.assertEqual(self.mixin.get_template_names(), ['wow_bidon*'])

    @patch('template_pdf.mixins.abstract.issubclass')
    def test_get_template_names_with_model(self, mock_issubclass):
        mock_issubclass.side_effect = lambda *args: True
        self.mixin.template_name_suffix = '.odt'
        self.mixin.object = None
        self.mixin.model = self.object
        self.assertEqual(self.mixin.get_template_names(), ['wow_bidon*'])

    def test_get_template_names_not_found(self):
        self.mixin.object = None
        with self.assertRaises(ImproperlyConfigured):
            self.mixin.get_template_names()
