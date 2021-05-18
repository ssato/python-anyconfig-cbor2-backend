================================
python-anyconfig-cbor2-backend
================================

.. image:: https://img.shields.io/pypi/v/anyconfig-cbor2-backend.svg
   :target: https://pypi.python.org/pypi/anyconfig-cbor2-backend/
   :alt: [Latest Verscbor2]

.. image:: https://github.com/ssato/python-anyconfig-cbor2-backend/workflows/Tests/badge.svg
   :target: https://github.com/ssato/python-anyconfig-cbor2-backend/actions?query=workflow%3ATests
   :alt: [Github Actions: Test status]

.. image:: https://img.shields.io/coveralls/ssato/python-anyconfig-cbor2-backend.svg
   :target: https://coveralls.io/r/ssato/python-anyconfig-cbor2-backend
   :alt: Coverage Status

.. image:: https://landscape.io/github/ssato/python-anyconfig-cbor2-backend/master/landscape.png
   :target: https://landscape.io/github/ssato/python-anyconfig-cbor2-backend/master
   :alt: Code Health

This is a backend parser module for python-anyconfig to support to load and
dump CBOR files w/ using cbor2, https://pypi.python.org/pypi/cbor2.

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

- Pre-built Binary RPMs from my copr repos, https://copr.fedoraproject.org/coprs/ssato/python-anyconfig/

    ::

      # Example commands to install pre-built RPMs
      $ sudo dnf copr enable ssato/python-anyconfig
      $ sudo dnf install -y python3-anyconfig-cbor2-backend

- PyPI: pip3 install anyconfig-cbor2-backend
- pip from git repo: pip3 install git+https://github.com/ssato/python-anyconfig-cbor2-backend/
- Build SRPMs, RPMs and install it: python3 setup.py bdist_rpm --source-only && mock dist/python3-anyconfig-\*-backend-<ver_dist>.src.rpm
- Others: try usual ways to build and/or install python modules such like 'python setup.py bdist', etc.

.. vim:sw=2:ts=2:et:
