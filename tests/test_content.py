from tests.base import TestCase
from website_tester.website_tester import WebSiteTester


class TestContent(TestCase):
    """Testclass for checking if content is up."""

    def setUp(self):
        self.website_tester = WebSiteTester("http://www.google.com")
        self.broken_website_tester = WebSiteTester("http://www.blankwebsite.com/")

    def test_can_reach(self):
        """Tests if reachable content is correctly detected."""
        is_up = self.website_tester.content_is_up()
        is_down = self.broken_website_tester.content_is_up()

        self.assertEqual(is_up, True)
        self.assertEqual(is_down, False)

    def test_can_reach_all(self):
        """Extensive test if reachable content is correctly detected."""
        website_tester_404 = WebSiteTester("http://www.google.com/adssdf/")
        is_up = website_tester_404.content_is_up()

        self.assertEqual(is_up, False)
