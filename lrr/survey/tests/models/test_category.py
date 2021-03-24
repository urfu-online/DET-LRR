# -*- coding: utf-8 -*-

from lrr.survey.models.category import Category
from lrr.survey.tests import BaseTest


class TestCategory(BaseTest):
    def test_unicode(self):
        """ Unicode is not None and do not raise error. """
        cat = Category.objects.all()[0]
        self.assertIsNotNone(cat)

    def test_slugify(self):
        """ Slugify is not None and do not raise error. """
        cat = Category.objects.all()[0]
        self.assertIsNotNone(cat.slugify())
