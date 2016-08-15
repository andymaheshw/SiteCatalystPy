========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor|
        |
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-pyadobemc/badge/?style=flat
    :target: https://readthedocs.org/projects/python-pyadobemc
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/randyzwitch/python-pyadobemc.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/randyzwitch/python-pyadobemc

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/randyzwitch/python-pyadobemc?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/randyzwitch/python-pyadobemc

.. |version| image:: https://img.shields.io/pypi/v/pyadobemc.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pyadobemc

.. |downloads| image:: https://img.shields.io/pypi/dm/pyadobemc.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/pyadobemc

.. |wheel| image:: https://img.shields.io/pypi/wheel/pyadobemc.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pyadobemc

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pyadobemc.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pyadobemc

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pyadobemc.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pyadobemc


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD license

Installation
============

::

    pip install pyadobemc

Documentation
=============

https://python-pyadobemc.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox


            
