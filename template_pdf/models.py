from django.contrib.contenttypes.models import ContentType
from django.db.models import (PROTECT, CharField, FileField, ForeignKey,
                              Manager, Model)

FILE_EXTENSIONS = (
    ('odt', 'odt'),
    ('html', 'html'),
)


def upload_path_handler(instance, filename):
    model_class = instance.content_type.model_class()
    return 'templates/{0}/{1}_{2}.{3}'.format(
        instance.format,
        model_class._meta.app_label,
        model_class._meta.model_name,
        instance.format,
    )


class DocumentTemplate(Model):
    name = CharField(max_length=255)
    format = CharField(max_length=255, choices=FILE_EXTENSIONS)
    documenttemplate = FileField(upload_to=upload_path_handler)

    content_type = ForeignKey(ContentType, on_delete=PROTECT)

    objects = Manager()
