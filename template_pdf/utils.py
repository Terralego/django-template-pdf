from enum import Enum


class LibreOfficeMimeTypes(Enum):
    odt = 'application/vnd.oasis.opendocument.text'
    ott = 'application/vnd.oasis.opendocument.text-template'
    oth = 'application/vnd.oasis.opendocument.text-web'
    odm = 'application/vnd.oasis.opendocument.text-master'
    otm = 'application/vnd.oasis.opendocument.text-master-template'
    odg = 'application/vnd.oasis.opendocument.graphics'
    otg = 'application/vnd.oasis.opendocument.graphics-template'
    odp = 'application/vnd.oasis.opendocument.presentation'
    otp = 'application/vnd.oasis.opendocument.presentation-template'
    ods = 'application/vnd.oasis.opendocument.spreadsheet'
    ots = 'application/vnd.oasis.opendocument.spreadsheet-template'
    odc = 'application/vnd.oasis.opendocument.chart'
    odf = 'application/vnd.oasis.opendocument.formula'
    odi = 'application/vnd.oasis.opendocument.image'

    @staticmethod
    def is_member(mime_type):
        for member in LibreOfficeMimeTypes:
            if member.value == mime_type:
                return True
        return False

    @staticmethod
    def keys():
        return [e.name for e in LibreOfficeMimeTypes]

    @staticmethod
    def values():
        return [e.value for e in LibreOfficeMimeTypes]

    @staticmethod
    def to_tuple():
        return tuple([(e.value, e.name) for e in LibreOfficeMimeTypes])
