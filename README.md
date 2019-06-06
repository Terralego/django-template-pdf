[![Build Status](https://travis-ci.org/Terralego/django-template-pdf.svg?branch=master)](https://travis-ci.org/Terralego/django-template-pdf)

# django-template-pdf
Django template, reponse and view to generate PDF

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
