#
# Copyright (C) 2018 - 2021 Satoru SATOH <satoru.satoh @ gmail.com>
# License: MIT
#
# pylint: disable=too-many-ancestors
r"""CBOR backend:

- Format to support: CBOR, http://cbor.io, https://tools.ietf.org/html/rfc7049
- Requirements: cbor2, https://pypi.python.org/pypi/cbor2
- Development Status :: 3 - Alpha
- Limitations: None obvious
- Special options:

  - All options of cbor2.load{s,} and cbor2.dump{s,} should work.
  - See also: https://github.com/agronholm/cbor2/blob/master/cbor2/

Changelog:
.. versionchanged:: 0.0.4

   - enhancement: add _cid to allow users to chose this than cbor explicitely

.. versionchanged:: 0.0.3

   - fix: follow internal API changes of the argument for load/dump functions

.. versionadded:: 0.0.2
"""
import cbor2

import anyconfig.backend.base


class Parser(anyconfig.backend.base.StringStreamFnParser,
             anyconfig.backend.base.BinaryLoaderMixin,
             anyconfig.backend.base.BinaryDumperMixin):
    """Parser for CBOR files.
    """
    _type = "cbor"
    _cid = "cbor2"
    _priority = 10  # Gives higher precedence than cbor.
    _extensions = ["cbor"]
    _loads_opts = ["tag_hook", "object_hook"]
    _dump_opts = ["datetime_as_timestamp", "timezone", "value_sharing",
                  "default"]

    _load_from_string_fn = anyconfig.backend.base.to_method(cbor2.loads)
    _load_from_stream_fn = anyconfig.backend.base.to_method(cbor2.load)
    _dump_to_string_fn = anyconfig.backend.base.to_method(cbor2.dumps)
    _dump_to_stream_fn = anyconfig.backend.base.to_method(cbor2.dump)

# vim:sw=4:ts=4:et:
