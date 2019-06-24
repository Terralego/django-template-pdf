from re import compile as re_compile

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from rest_framework.serializers import (CharField, ModelSerializer,
                                        SerializerMethodField, ValidationError)

from template_pdf.models import DocumentTemplate


class DocumentTemplateSerializer(ModelSerializer):
    content_type = CharField(max_length=255, write_only=True)
    associated_object = SerializerMethodField()

    class Meta:
        model = DocumentTemplate
        fields = ('pk', 'name', 'format', 'documenttemplate', 'content_type',
                  'associated_object')
        extra_kwargs = {
            'documenttemplate': {'write_only': True},
        }

    def get_associated_object(self, obj):
        model_class = obj.content_type.model_class()
        return {
            'app_label': model_class._meta.app_label,
            'model_name': model_class._meta.model_name,
        }

    def validate_content_type(self, data):
        regex = re_compile(r'^(?P<app_label>[^\.]+)\.(?P<model_name>[^<]+)$')
        match = regex.search(data)
        try:
            app_label = match.group('app_label')
            model_name = match.group('model_name')
        except AttributeError:
            raise ValidationError('Bad content type.')
        model_class = apps.get_model(app_label, model_name=model_name)
        content_type = ContentType.objects.get_for_model(model_class)
        return content_type
