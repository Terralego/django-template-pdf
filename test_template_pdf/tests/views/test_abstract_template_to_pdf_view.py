from django.test import TestCase, RequestFactory
from django.http import Http404

from template_pdf.views import AbstractTemplateToPdfView
from test_template_pdf.models import Bidon
from test_template_pdf.tests.backends.backend_settings import ODT_TEMPLATE_PATH


class TemplateToPdfView(AbstractTemplateToPdfView):
    queryset = Bidon.objects.all()
    template_engine = 'odt'


class TemplateToPdfViewWithTemplateName(AbstractTemplateToPdfView):
    queryset = Bidon.objects.all()
    template_engine = 'odt'
    template_name = ODT_TEMPLATE_PATH


class TemplateToPdfViewWithBadTemplateName(AbstractTemplateToPdfView):
    queryset = Bidon.objects.all()
    template_engine = 'odt'
    template_name = 'bad/path'


class TestAbstractTemplateToPdfView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.object = Bidon.objects.create(name='Michel')
        self.request = self.factory.get('')

    def test_view_works(self):
        response = TemplateToPdfView.as_view()(self.request, **{'pk': 1}).render()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(54368, len(response.content))

    def test_view_bad_object(self):
        with self.assertRaises(Http404):
            TemplateToPdfView.as_view()(self.request, **{'pk': 2}).render()

    def test_view_template_name_defined_works(self):
        response = (
            TemplateToPdfViewWithTemplateName
            .as_view()(self.request, **{'pk': 1})
            .render()
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(54368, len(response.content))

    def test_view_bad_template_name(self):
        with self.assertRaises(Http404):
            TemplateToPdfViewWithBadTemplateName.as_view()(self.request, **{'pk': 2}).render()
