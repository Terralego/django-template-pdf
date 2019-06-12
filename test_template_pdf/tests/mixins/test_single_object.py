from django.http import Http404
from django.test import TestCase

from template_pdf.mixins import SingleObjectMixin
from test_template_pdf.models import Bidon


class TestSingleObject(TestCase):

    def setUp(self):
        self.mixin = SingleObjectMixin()
        self.object = Bidon.objects.create(name='Michel')

    def test_get_object_with_queryset(self):
        self.mixin.kwargs = {'pk': 1}
        obj = self.mixin.get_object(queryset=Bidon.objects.all())
        self.assertEqual(obj, self.object)

    def test_get_object_with_no_queryset(self):
        self.mixin.kwargs = {'pk': 1}
        self.mixin.get_queryset = lambda *args: Bidon.objects.all()
        obj = self.mixin.get_object()
        self.assertEqual(obj, self.object)

    def test_get_object_content_field_is_none(self):
        self.mixin.kwargs = {}
        with self.assertRaisesRegex(AttributeError,
                                    'Generic detail view SingleObjectMixin' +
                                    ' must be called with an object.'):
            self.mixin.get_object(queryset=Bidon.objects.all())

    def test_get_object_multiple_objects(self):
        Bidon.objects.create(name='Michel')
        self.mixin.lookup_field = 'name'
        self.mixin.lookup_field_url_kwargs = 'name'
        self.mixin.kwargs = {'name': 'Michel'}
        with self.assertRaisesRegex(AttributeError,
                                    'The field must be a primary key. Multiple' +
                                    ' objects are prohibited.'):
            self.mixin.get_object(queryset=Bidon.objects.all())

    def test_get_object_unknown_object(self):
        self.mixin.kwargs = {'pk': 2}
        with self.assertRaises(Http404):
            self.mixin.get_object(queryset=Bidon.objects.all())
