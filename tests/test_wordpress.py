# from tests.base import TestCase
# from website_tester.wordpress import WordpressTester


# class TestWordpress(TestCase):
#     """Testclass for wordpress checker."""

#     def setUp(self):
#         self.website_tester = WordpressTester("http://www.google.com")

#     def test_can_enumerate(self):
#         """Tests if enumeration of wordpress accounts is correctly detected."""
#         can_enumerate = self.website_tester.can_enumerate()
#         self.assertEqual(can_enumerate, True)

#     def test_leaks_version(self):
#         """Tests if wordpress version leak is correctly detected."""
#         leaks_version = self.website_tester.leaks_version()
#         self.assertEqual(leaks_version, True)

#     def test_can_access_nonpublic_content(self):
#         """Tests if content that should not be public, but can be accessed is
#         correctly detected."""
#         can_access = self.website_tester.can_access_nonpulic_content()
#         self.assertEqual(can_access, True)

#     def test_can_post_comment(self):
#         """Tests if possibility of unmoderated comment posting is correctly
#         detected."""
#         can_comment = self.website_tester.can_post_unmoderated_comment()
#         self.assertEqual(can_comment, True)

#     def test_can_pingback(self):
#         """Tests if pingback and trackback possibility is correctly detected."""
#         can_pingback = self.website_tester.can_pingback()
#         self.assertEqual(can_pingback, True)
