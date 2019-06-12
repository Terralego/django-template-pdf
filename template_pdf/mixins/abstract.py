from django.core.exceptions import ImproperlyConfigured
from django.db.models import Model
from django.views.generic.base import TemplateResponseMixin


class AbstractTemplateResponseMixin(TemplateResponseMixin):
    template_name_field = None
    template_name_suffix = None

    def get_template_names(self):
        try:
            names = super().get_template_names()
        except ImproperlyConfigured:
            names = []

            if self.object and self.template_name_field:
                name = getattr(self.object, self.template_name_field, None)
                if name:
                    names.insert(0, name)

            if isinstance(self.object, Model):
                object_meta = self.object._meta
                names.append("%s_%s*%s" % (
                    object_meta.app_label,
                    object_meta.model_name,
                    self.template_name_suffix
                ))
            elif getattr(self, 'model', None) is not None and issubclass(self.model, Model):
                names.append("%s_%s*%s" % (
                    self.model._meta.app_label,
                    self.model._meta.model_name,
                    self.template_name_suffix
                ))

            if not names:
                raise

        return names
