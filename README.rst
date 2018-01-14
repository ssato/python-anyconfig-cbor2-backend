================================
python-anyconfig-cbor2-backend
================================

.. image:: https://img.shields.io/pypi/v/anyconfig-cbor2-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-cbor2-backend/
   :alt: [Latest Verscbor2]

.. image:: https://img.shields.io/travis/ssato/python-anyconfig-cbor2-backend.svg
   :target: https://travis-ci.org/ssato/python-anyconfig-cbor2-backend
   :alt: Test status

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-cbor2-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-cbor2-backend
   :alt: Coverage Status

.. image:: https://landscape.io/github/ssato/python-anyconfig-cbor2-backend/master/landscape.png
   :target: https://landscape.io/github/ssato/python-anyconfig-cbor2-backend/master
   :alt: Code Health

This is a backend module for python-anyconfig to support to load and dump CBOR
files w/ using cbor2, https://pypi.python.org/pypi/cbor2.

- Author: Satoru SATOH <ssato@redhat.com>
- License: MIT

SEE ALSO:

- python-anyconfig: https://pypi.python.org/pypi/anyconfig
- CBOR spec: http://cbor.io

- Download:

  - PyPI: https://pypi.python.org/pypi/anyconfig-cbor2-backend
  - Copr RPM repos: https://copr.fedoraproject.org/coprs/ssato/python-anyconfig/

Build & Install
================

If you're Fedora or Red Hat Enterprise Linux user, try::

  $ python setup.py srpm && mock dist/<package>-<ver_dist>.src.rpm
  
or::

  $ python setup.py rpm

and install built RPMs. 

Otherwise, try usual ways to build and/or install python modules such like
'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:
