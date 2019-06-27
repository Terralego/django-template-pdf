from django.test import TestCase

from template_pdf.utils import LibreOfficeMimeTypes


class TestUtils(TestCase):

    def test_libreoffice_enum_is_member(self):
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.text'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.text-template'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.text-web'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.text-master'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.text-master-template'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.graphics'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.graphics-template'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.presentation'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.presentation-template'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.spreadsheet'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.spreadsheet-template'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.chart'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.formula'))
        self.assertTrue(LibreOfficeMimeTypes.is_member(
            'application/vnd.oasis.opendocument.image'))

        self.assertFalse(LibreOfficeMimeTypes.is_member('Michel'))
        self.assertFalse(LibreOfficeMimeTypes.is_member('text/html'))

    def test_libreoffice_enum_keys(self):
        self.assertEqual(
            LibreOfficeMimeTypes.keys(),
            ['odt', 'ott', 'oth', 'odm', 'otm', 'odg', 'otg', 'odp', 'otp', 'ods', 'ots', 'odc',
             'odf', 'odi']
        )

    def test_libreoffice_enum_values(self):
        self.assertEqual(
            LibreOfficeMimeTypes.values(),
            ['application/vnd.oasis.opendocument.text',
             'application/vnd.oasis.opendocument.text-template',
             'application/vnd.oasis.opendocument.text-web',
             'application/vnd.oasis.opendocument.text-master',
             'application/vnd.oasis.opendocument.text-master-template',
             'application/vnd.oasis.opendocument.graphics',
             'application/vnd.oasis.opendocument.graphics-template',
             'application/vnd.oasis.opendocument.presentation',
             'application/vnd.oasis.opendocument.presentation-template',
             'application/vnd.oasis.opendocument.spreadsheet',
             'application/vnd.oasis.opendocument.spreadsheet-template',
             'application/vnd.oasis.opendocument.chart',
             'application/vnd.oasis.opendocument.formula',
             'application/vnd.oasis.opendocument.image']
        )

    def test_libreoffice_enum_to_tuple(self):
        self.assertEqual(
            LibreOfficeMimeTypes.to_tuple(),
            (('application/vnd.oasis.opendocument.text', 'odt'),
             ('application/vnd.oasis.opendocument.text-template', 'ott'),
             ('application/vnd.oasis.opendocument.text-web', 'oth'),
             ('application/vnd.oasis.opendocument.text-master', 'odm'),
             ('application/vnd.oasis.opendocument.text-master-template', 'otm'),
             ('application/vnd.oasis.opendocument.graphics', 'odg'),
             ('application/vnd.oasis.opendocument.graphics-template', 'otg'),
             ('application/vnd.oasis.opendocument.presentation', 'odp'),
             ('application/vnd.oasis.opendocument.presentation-template', 'otp'),
             ('application/vnd.oasis.opendocument.spreadsheet', 'ods'),
             ('application/vnd.oasis.opendocument.spreadsheet-template', 'ots'),
             ('application/vnd.oasis.opendocument.chart', 'odc'),
             ('application/vnd.oasis.opendocument.formula', 'odf'),
             ('application/vnd.oasis.opendocument.image', 'odi'))
        )
