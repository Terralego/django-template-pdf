from django.test import TestCase

from template_pdf.mixins import SingleObjectMixin


class Meta:
    app_label = 'wow'
    model_name = 'bidon'


class Bidon:
    def __init__(self, name, template_name):
        self.name = name
        self.template_name = template_name
        self._meta = Meta()


class ModelSet:
    def __init__(self, f=None):
        self.filters = f

    def filter(self, **kwargs):
        self.filters = kwargs
        return self

    def count(self):
        return 1

    def get(self):
        return 'That is an object!'


class TestSingleObject(TestCase):

    def setUp(self):
        self.mixin = SingleObjectMixin()
        self.object = Bidon('Michel', 'Pierre')

    def test_get_object_with_queryset(self):
        self.mixin.kwargs = {'pk': 1}
        obj = self.mixin.get_object(queryset=ModelSet())
        self.assertEqual(obj, 'That is an object!')

    def test_get_object_with_no_queryset(self):
        self.mixin.kwargs = {'pk': 1}
        self.mixin.get_queryset = lambda *args: ModelSet()
        obj = self.mixin.get_object()
        self.assertEqual(obj, 'That is an object!')

    def test_get_object_content_field_is_none(self):
        self.mixin.kwargs = {}
        with self.assertRaisesRegex(AttributeError,
                                    'Generic detail view SingleObjectMixin' +
                                    ' must be called with an object.'):
            self.mixin.get_object(queryset=ModelSet())

    def test_get_object_multiple_objects(self):
        self.mixin.kwargs = {'pk': 1}
        model_set = ModelSet()
        model_set.count = lambda *args: 2
        with self.assertRaisesRegex(AttributeError,
                                    'The field must be a primary key. Multiple' +
                                    ' objects are prohibited.'):
            self.mixin.get_object(queryset=model_set)
