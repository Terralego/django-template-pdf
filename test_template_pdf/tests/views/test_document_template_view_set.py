from shutil import rmtree

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from test_template_pdf.models import Bidon
from test_template_pdf.tests.backends.backend_settings import ODT_TEMPLATE_PATH


class TestDocumentTemplateViewSet(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('12345')
        self.user.save()
        self.client.login(username='testuser', password='12345')

    def test_bad_content_type(self):
        template = SimpleUploadedFile('template1.odt', b'Pierre !',
                                      content_type='application/vnd.oasis.opendocument.text')
        response = self.client.post(reverse('document-list'),
                                    data={'name': 'Template', 'format': 'odt',
                                          'documenttemplate': template,
                                          'content_type': 'test_template_pdf-Bidon'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content, b'{"content_type":["Bad content type."]}')

    # def test_list_by_model(self):
    #     template1 = SimpleUploadedFile('template.odt', b'Pierre !',
    #                                    content_type='application/vnd.oasis.opendocument.text')
    #     response = self.client.post(reverse('document-list'),
    #                                 data={'name': 'Template1', 'format': 'odt',
    #                                       'documenttemplate': template1,
    #                                       'content_type': 'test_template_pdf.Bidon'})
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(
    #         b''.join([
    #             b'{"pk":1,"name":"Template1","format":"odt","associated_object":{"app_label":',
    #             b'"test_template_pdf","model_name":"bidon"}}',
    #         ]),
    #         response.content
    #     )
    #     list_by_model_response = self.client.get(
    #         reverse('document-list-by-model',
    #                 kwargs={'app_label': 'test_template_pdf', 'model_name': 'Bidon'}))
    #     self.assertEqual(list_by_model_response.status_code, 200)
    #     self.assertEqual(
    #         list_by_model_response.content,
    #         b''.join([
    #             b'[{"pk":1,"name":"Template1","format":"odt","associated_object":{"app_label":',
    #             b'"test_template_pdf","model_name":"bidon"}}]',
    #         ])
    #     )
    #     template2 = SimpleUploadedFile('template2.odt', b'Michel !',
    #                                    content_type='application/vnd.oasis.opendocument.text')
    #     self.client.post(reverse('document-list'),
    #                      data={'name': 'Template2', 'format': 'odt',
    #                            'documenttemplate': template2,
    #                            'content_type': 'test_template_pdf.Bidon'})
    #     list_by_model_response = self.client.get(
    #         reverse('document-list-by-model',
    #                 kwargs={'app_label': 'test_template_pdf', 'model_name': 'Bidon'}))
    #     self.assertEqual(list_by_model_response.status_code, 200)
    #     self.assertEqual(
    #         list_by_model_response.content,
    #         b''.join([
    #             b'[{"pk":1,"name":"Template1","format":"odt","associated_object":{"app_label":',
    #             b'"test_template_pdf","model_name":"bidon"}},{"pk":2,"name":"Template2",',
    #             b'"format":"odt","associated_object":{"app_label":"test_template_pdf",',
    #             b'"model_name":"bidon"}}]',
    #         ])
    #     )
    #     template3 = SimpleUploadedFile('template3.odt', b'Bernard !',
    #                                    content_type='application/vnd.oasis.opendocument.text')
    #     self.client.post(reverse('document-list'),
    #                      data={'name': 'Template3', 'format': 'odt',
    #                            'documenttemplate': template3,
    #                            'content_type': 'test_template_pdf.BidonBis'})
    #     list_by_model_response = self.client.get(
    #         reverse('document-list-by-model',
    #                 kwargs={'app_label': 'test_template_pdf', 'model_name': 'Bidon'}))
    #     self.assertEqual(list_by_model_response.status_code, 200)
    #     self.assertEqual(
    #         list_by_model_response.content,
    #         b''.join([
    #             b'[{"pk":1,"name":"Template1","format":"odt","associated_object":{"app_label":',
    #             b'"test_template_pdf","model_name":"bidon"}},{"pk":2,"name":"Template2",',
    #             b'"format":"odt","associated_object":{"app_label":"test_template_pdf",',
    #             b'"model_name":"bidon"}}]',
    #         ])
    #     )
    #     self.assertEqual(
    #         self.client.get(reverse('document-list')).content,
    #         b''.join([
    #             b'[{"pk":1,"name":"Template1","format":"odt","associated_object":{',
    #             b'"app_label":"test_template_pdf","model_name":"bidon"}},{"pk":2,"name":',
    #             b'"Template2","format":"odt","associated_object":{"app_label":"test_template_pdf"',
    #             b',"model_name":"bidon"}},{"pk":3,"name":"Template3","format":"odt",',
    #             b'"associated_object":{"app_label":"test_template_pdf","model_name":"bidonbis"}}]',
    #         ])
    #     )
    #     rmtree('templates')

    # def test_render(self):
    #     Bidon.objects.create(name='Michel')
    #     with open(ODT_TEMPLATE_PATH, 'rb') as reader:
    #         template = SimpleUploadedFile('template1.odt', reader.read(),
    #                                       content_type='application/vnd.oasis.opendocument.text')
    #     self.client.post(reverse('document-list'),
    #                      data={'name': 'Template', 'format': 'odt',
    #                            'documenttemplate': template,
    #                            'content_type': 'test_template_pdf.Bidon'})
    #     response = self.client.get(reverse('document-render', kwargs={'pk': 1, 'object_id': 1}))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response._content_type_for_repr, ', "application/pdf"')
    #     self.assertEqual(54368, len(response.content))
    #     rmtree('templates')
