from glob import glob
from os.path import isfile, join

from django.template import Template
from django.template.backends.base import BaseEngine
from django.template.loader import TemplateDoesNotExist


class AbstractEngine(BaseEngine):
    """
    Gives the architecture of a basic template engine and two methods implemented: \
``get_template_path`` and ``from_string``.

    Must be specified:
    * ``app_dirname``, the folder name which contains the templates,
    * ``template_class``, your own template class with a ``render`` method.

    ``get_template`` must be implemented.
    """
    app_dirname = None
    template_class = None

    def __init__(self, params):
        params = params.copy()
        self.options = params.pop('OPTIONS')
        super().__init__(params)

    def from_string(self, template_code, **kwargs):
        return self.template_class(Template(template_code), **kwargs)

    def get_template_path(self, template_name):
        """
        Check if a template named ``template_name`` can be found in a list of directories. Returns \
the path if the file exists or raises ``TemplateDoesNotExist`` otherwise.
        """
        if isfile(template_name):
            return template_name
        template_path = None
        for directory in self.template_dirs:
            abstract_path = join(directory, template_name)
            path = glob(abstract_path)
            if path:
                template_path = path[0]
                break
        if template_path is None:
            raise TemplateDoesNotExist(f'Unknown: {template_name}')
        return template_path

    def get_template(self, template_name):
        raise NotImplementedError()
