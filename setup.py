#!/usr/bin/env python
from os.path import abspath, dirname, join
from setuptools import setup

import template_pdf


HERE = abspath(dirname(__file__))
PACKAGES = ['template_pdf']
PACKAGE_DIR = {'template_pdf': 'template_pdf'}


def get_requires():
    requirements_f = open(join(HERE, 'requirements.txt'), 'r')
    install_requires = requirements_f.read().splitlines()
    requirements_f.close()
    return install_requires


setup(
    name='template_pdf',
    version=template_pdf.__version__,
    author_email=template_pdf.__email__,
    description='Django template, reponse and view to generate PDF.',
    long_description=open(join(HERE, 'README.md')).read()
    + '\n\n'
    + open(join(HERE, 'CHANGES.md')).read(),
    packages=PACKAGES,
    package_dir=PACKAGE_DIR,
    include_package_data=True,
    url='https://github.com/Terralego/django-template-pdf',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=get_requires(),
    entry_points={
        'console_scripts': [
            'convertor = template_pdf.pdf_convertor.server:main'
        ],
    },
)
