# -*- coding: utf8 -*-
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

from django.template import Template, Context, TemplateSyntaxError
from django.test import TestCase

from ..templatetags import mimetypes


class IconTestCase(TestCase):

    def test_icon_mimetype(self):
        self.assertEqual(mimetypes.icon("image/jpeg"), "/static/mimetypes/64x64/image-x-generic.png")

    def test_icon_mimetype_size(self):
        self.assertEqual(mimetypes.icon("image/jpeg", size="32x32"), "/static/mimetypes/32x32/image-x-generic.png")


class TagTestCase(TestCase):

    def render(self, template, **kwargs):
        self.context = Context(dict_=kwargs)
        return Template("{% load mimetypes %}" + template).render(self.context)

    def test_mimetype(self):
        self.assertEqual(self.render("""{% icon "image/jpeg" %}"""),
                         "/static/mimetypes/64x64/image-x-generic.png")

    def test_mimetype_size(self):
        self.assertEqual(self.render("""{% icon "image/jpeg" "32x32" %}"""),
                         "/static/mimetypes/32x32/image-x-generic.png")

    def test_mimetype_size_var(self):
        self.assertEqual(self.render("""{% icon "image/jpeg" size %}""", size="16x16"),
                         "/static/mimetypes/16x16/image-x-generic.png")

    def test_mimetype_var(self):
        self.assertEqual(self.render("""{% icon mimetype %}""", mimetype="image/jpeg"),
                         "/static/mimetypes/64x64/image-x-generic.png")

    def test_mimetype_var_size(self):
        self.assertEqual(self.render("""{% icon mimetype "16x16" %}""", mimetype="image/jpeg"),
                         "/static/mimetypes/16x16/image-x-generic.png")

    def test_mimetype_var_size_var(self):
        self.assertEqual(self.render("""{% icon mimetype size %}""", mimetype="image/jpeg", size="24x24"),
                         "/static/mimetypes/24x24/image-x-generic.png")

    def test_mimetype_as_varname(self):
        self.assertEqual(self.render("""{% icon "application/pdf" as pdf_icon %}"""), "")
        self.assertEqual(self.context['pdf_icon'], "/static/mimetypes/64x64/application-pdf.png")

    def test_mimetype_size_as_varname(self):
        self.assertEqual(self.render("""{% icon "application/pdf" "32x32" as pdf_icon %}"""), "")
        self.assertEqual(self.context['pdf_icon'], "/static/mimetypes/32x32/application-pdf.png")

    def test_mimetype_size_var_as_varname(self):
        self.assertEqual(self.render("""{% icon "application/pdf" size as pdf_icon %}""", size="16x16"), "")
        self.assertEqual(self.context['pdf_icon'], "/static/mimetypes/16x16/application-pdf.png")

    def test_mimetype_var_as_varname(self):
        self.assertEqual(self.render("""{% icon mimetype as pdf_icon %}""", mimetype="application/pdf"), "")
        self.assertEqual(self.context['pdf_icon'], "/static/mimetypes/64x64/application-pdf.png")

    def test_mimetype_var_size_as_varname(self):
        self.assertEqual(self.render("""{% icon mimetype "32x32" as pdf_icon %}""", mimetype="application/pdf"), "")
        self.assertEqual(self.context['pdf_icon'], "/static/mimetypes/32x32/application-pdf.png")

    def test_mimetype_var_size_var_as_varname(self):
        self.assertEqual(self.render("""{% icon mimetype size as pdf_icon %}""", mimetype="application/pdf",
                                     size="16x16"),
                         "")
        self.assertEqual(self.context['pdf_icon'], "/static/mimetypes/16x16/application-pdf.png")

    def test_errors(self):
        self.assertRaises(TemplateSyntaxError, self.render, """{% icon %}""")
        self.assertRaises(TemplateSyntaxError, self.render, """{% icon "image/jpeg" as %}""")
        self.assertRaises(TemplateSyntaxError, self.render, """{% icon "image/jpeg" "32x32" as %}""")
