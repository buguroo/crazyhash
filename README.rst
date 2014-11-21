crazyhash
=========

Crazyhash is a *natural language hashing library* for Python.

Built on top of well known hashing functions, _crazyhash_ replaces the
hard-to-remember output data by a sequence of words.


Usage example
-------------

.. code-block:: python

   >>> from crazyhash import countries_colors
   >>> h = countries_colors.Hasher()
   >>> h.update(b'INSERT-HERE-BINARY-DATA-TO-HASH')
   >>> h.digest()
   u'HAITI-CORAL'
   >>> from crazyhash import nato_capitals_nato
   >>> h = nato_capitals_nato.Hasher()
   >>> h.update(b'INSERT-HERE-BINARY-DATA-TO-HASH')
   >>> h.digest()
   u'YANKEE-SANAA-GOLF'


Features
--------

- Word lists included (see below).
- Standard python hashlib API.
- Pure Python.
- Import hook system for easy usage.
- Easy to extend and customize.

  - Custom word lists.
  - Hash phrase length.
  - Interchangeable inner hashing function (default hashlib.sha1).


Current dictionaries
--------------------

- Animals
- Capitals
- Colors
- Countries
- Kamasutra
- Weather
