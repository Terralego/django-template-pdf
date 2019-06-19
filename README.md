[![Build Status](https://travis-ci.org/Terralego/django-template-pdf.svg?branch=master)](https://travis-ci.org/Terralego/django-template-pdf)

# django-template-pdf
Django template, response and view to generate PDF

# Quick start
## Document template

A model is available to store the templates. It contains the following fiels:
* `name`, `CharField`,
* `format`, `CharField` (html, odt, ott, oth, odm, otm, odg, otg, odp, otp, ods, ots, odc, odf, odi),
* `documenttemplate`, `FileField`,
* `content_type`, `ForeignKey(ContentType)`,

You can use it by adding in the settings:

```
INSTALLED_APP = [
    ...
    'template_pdf',
]
```

## Pdf converter

### Description

The pdf converter is a tool that will allow you to convert LibreOffice or Html documents to pdf.

### Installation

To start the local server, you must first create the Docker image.
If you are at the root of the project, run the following command:

```
docker build -t server ./template_pdf/pdf_convertor
```

Once done, you can launch a container by executing the following command:

```
docker run -itd -p "127.0.0.1:9999:9999" server
```

## Template backends

### Create your own backend

An abstract template engine is at your disposal, you can use it by importing it as follows:

```
from template_pdf.backends.abstract import AbstractEngine
```

Some functions that can help you build your engine can be imported as follows:

```
from template_pdf.backends.utils import ...
```

We advice you to create a module named `backends`.

For more information and examples, please read the doc.

### Use a specific template backend

In the settings modify:

```
INSTALLED_APPS = [
    ...
    'template_pdf',
]

...

TEMPLATES = [
    {
        'BACKEND': 'template_pdf.backends.odt.OdtEngine',
        'DIRS': [
        ],
        'APP_DIRS': True,
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

You can now create a view as follows:

```
from template_pdf.views import AbstractTemplateToPdfView

from .models import YourModel


class TemplateView(AbstractTemplateToPdfView):
    model = YourModel
```

For more information and examples, please read the doc.

# Good practices

## Set up a virtual environment

If virtualenv is not installed, run the following command in your terminal:
```
pip install virtualenv
```

Then create a virtual environment by running:
```
virtualenv ./venv
```

Activate it by running:
```
source ./venv/bin/activate
```

## Tool for style guide enforcement

**It is advisable to use a tool for style guide enforcement.**

### Flake8

If your virtual environment is not active, run:
```
source ./venv/bin/activate
```

Install `flake8` by running:
```
pip install flake8
```

If you use vscode, you can configure it to use `flake8`:
```
ctrl + maj + p > Python: select linter
```

## Linting and tests

**It is advisable to do the following checks before committing anything.**

You can now install `tox` by running:
```
pip install tox
```

Run the tests and linter by running:
```
tox
```
