# -*- coding: utf-8 -*-
# Copyright 2013 Bors Ltd
# This file is part of django-icons-mimetypes.
#
#    django-icons-mimetypes is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Foobar is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
from __future__ import absolute_import, print_function, unicode_literals

from django.test import TestCase

from .. import icons


class IconsTestCase(TestCase):

    def test_cache(self):
        self.assertIn(("64x64", icons.ICON_FOLDER), icons.ICONS_CACHE)

    def test_get_icon(self):
        # Folder
        self.assertEqual(icons.get_icon(None), "/static/mimetypes/64x64/folder.png")

        # Regular
        self.assertEqual(icons.get_icon("application/pdf"), "/static/mimetypes/64x64/application-pdf.png")

        # Mimetype fallback
        self.assertEqual(icons.get_icon("application/rtf"), "/static/mimetypes/64x64/x-office-document.png")

        # Main part fallback
        self.assertEqual(icons.get_icon("image/jpeg"), "/static/mimetypes/64x64/image-x-generic.png")

        # Unknown
        self.assertEqual(icons.get_icon("foo/bar"), "/static/mimetypes/64x64/application-x-executable.png")
