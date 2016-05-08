from website_tester.website_tester import WebSiteTester


class WordpressTester(WebSiteTester):
    """Tests for Wordpress blogs."""

    def can_access_nonpulic_content(self):
        """Check if content that's not supposed to be public can be accessed."""
        return False

    def can_enumerate(self):
        """Check if Wordpress user accounts can be enumerated."""
        return False

    def can_pingback(self):
        """Check if pingbacks are possible."""
        return False

    def can_post_unmoderated_comment(self):
        """Check if comments can be posted without moderation."""
        return False

    def leaks_version(self):
        """Check if Wordpress version is leaked."""
        return False
