# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = (
    'Development Status :: 4 - Beta',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'License :: OSI Approved :: MIT License',
)

required = ('pandas', 'python-dateutil', 'pytz', 'requests', 'six')

kw = {
    'name': 'AdobeAnalytics',
    'version': '0.1.0',
    'description': 'A Python wrapper for the Adobe Analytics API',
    'author': 'Andy Maheshwari, Randy Zwitch',
    'author_email': 'andymaheshw@gmail.com',
    'license': 'MIT License',
    'url': 'https://github.com/andymaheshw/AdobeAnalytics',
    'keywords': 'digital analytics',
    'install_requires': required,
    'zip_safe': True,
}

setup(**kw)
