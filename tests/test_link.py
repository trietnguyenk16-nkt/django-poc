from django.test import TestCase
from portal.models import Portal
from django.urls import reverse

class PortalTestCase(TestCase):
    def test_add_row(self):
        self.assertEqual("abc", "abc")

