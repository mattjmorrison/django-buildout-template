
from setuptools import setup

setup(
    name="django-buildout",
    version="dev",
    description="Template application for Django and Buildout",
    author="Matthew J. Morrison",

    package_dir={'': 'src'},
    install_requires = (
        'mock',
        'lettuce',
        'south',
        'django-debug-toolbar',
    ),
)
