import requests


class WebSiteTester:
    """Class for testing website functionality."""
    def __init__(self, url):
        """Initialize class with base url."""
        self.url = url
        self.req = requests.get(url)

    def check_status_code(self):
        """Checks if the website returns a valid status code (i.e. not 4xx or
        5xx). A valid status code is defined as requests.codes.ok"""
        return (self.req.status_code == requests.codes.ok)

    def is_up(self):
        return self.check_status_code()
