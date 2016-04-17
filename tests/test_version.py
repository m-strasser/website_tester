#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of website_tester.
# https://github.com/m-strasser/website_tester

# Licensed under the GPL license:
# http://www.opensource.org/licenses/GPL-license
# Copyright (c) 2016, Michael Strasser <mst1409@gmx.at>

from preggy import expect

from website_tester import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
