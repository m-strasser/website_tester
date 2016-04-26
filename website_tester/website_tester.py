import requests
import urltools
from bs4 import BeautifulSoup


class WebSiteTester:
    """Class for testing website functionality."""
    def __init__(self, url):
        """Initialize class with base url."""
        self.url = urltools.normalize(url)
        self.req = requests.get(self.url)
        self.soup = -1
        self.status_code = self.req.status_code

    @classmethod
    def check_status_code(cls, url):
        """Checks if the website returns a valid status code (i.e. not 4xx or
        5xx). A valid status code is defined as requests.codes.ok."""
        req = requests.get(urltools.normalize(url))
        status_code = req.status_code

        return ((status_code == requests.codes.ok), status_code, req)

    def is_up(self):
        """Checks if the website is reachable."""
        is_up, self.status_code, self.req = WebSiteTester.check_status_code(
            self.url)

        return is_up

    def content_is_up(self):
        """Checks if the websites content can be reached. This means it checks
        if the website contains some form of text in it's body tag."""
        if not self.is_up():
            return False
        if self.soup == -1:
            self.soup = BeautifulSoup(self.req.content, 'html.parser')

        body = self.soup.find("body")

        if self.soup.get_text() == '':
            return False
        elif body is None:
            return False
        elif self.soup.find("body").get_text() == '':
            return False
        else:
            return True

    def subcontent_is_up(self):
        """Checks if the first internal link (that's not the home url) can be
        reached and contains content."""
        self.links = self.soup.find_all("a")
        self.internal_links = [urltools.normalize(link.get('href'))
                               for link in self.links
                               if self.url in link.get('href') and
                               not urltools.compare(self.url, link.get('href'))]

        return False
