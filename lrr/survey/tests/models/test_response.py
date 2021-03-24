# -*- coding: utf-8 -*-

from lrr.survey.tests.models import BaseModelTest


class TestResponse(BaseModelTest):
    def test_unicode(self):
        """ Unicode generation. """
        self.assertIsNotNone(str(self.response))
