#!/usr/bin/env python
# -*- coding: utf-8; mode: python -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import re
import codecs
from setuptools import setup, find_packages

def read_file(fname):
    with codecs.open(fname, 'r', 'utf-8') as f:
        return f.read()

def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__\s*=\s*['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE
        , re.M )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))

NAME     = 'syncserver'

REQUIRES = [
    'mozsvc>=2.0.0rc1'
    , 'tokenserver>=2.0.0rc1'
    , 'pyramid'
    , 'requests'
    , 'zope.interface'
]

EXTRAS_REQUIRE = {}

TESTS_REQUIRES = [
    'webtest'
    , 'testfixtures'
]

ENTRY_POINTS = """
[paste.app_factory]
main = syncserver:main
"""

META_FILE        = read_file('syncserver/__init__.py')
LONG_DESCRIPTION = [ read_file(n) for n in ['README.rst', 'CHANGES.txt']]

setup(name                   = NAME
      , version              = find_meta('version')
      , description          = find_meta('description')
      , long_description     = '\n\n'.join(LONG_DESCRIPTION)
      , url                  = find_meta('url')
      , author               = find_meta('author')
      , author_email         = find_meta('author_email')
      , license              = find_meta('license')
      , keywords             = find_meta('keywords')
      , packages             = find_packages()
      , include_package_data = True
      , install_requires     = REQUIRES
      , extras_require       = EXTRAS_REQUIRE
      # unfortunately test is not supported by pip (only 'setup.py test')
      , tests_require        = TESTS_REQUIRES
      , test_suite           = NAME
      , zip_safe             = False
      , entry_points         = ENTRY_POINTS
      , classifiers          = [
          "Programming Language :: Python"
          , "Framework :: Pylons"
          , "Topic :: Internet :: WWW/HTTP"
          , "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
          , "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"
          , "Development Status :: 5 - Production/Stable"
          , ]
      , )

