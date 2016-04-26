from tests.base import TestCase
from website_tester.website_tester import WebSiteTester
import unittest


class TestStatusCode(TestCase):
    """Testclass for status code checker."""

    def setUp(self):
        self.website_tester = WebSiteTester("http://www.google.com")
        self.broken_website_tester = WebSiteTester(
            "http://www.google.com/asdfasdf/")

    def test_is_up(self):
        """See if running website is recognized as running."""
        is_up = self.website_tester.is_up()
        self.assertEqual(is_up, True)

    def test_is_down(self):
        """See if non-existent page is recognized as not running."""
        is_up = self.broken_website_tester.is_up()
        self.assertEqual(is_up, False)

    def test_get_statuscode(self):
        """See if statuscode is correctly saved."""
        self.assertEqual(self.website_tester.status_code, 200)
        self.assertEqual(self.broken_website_tester.status_code, 404)

