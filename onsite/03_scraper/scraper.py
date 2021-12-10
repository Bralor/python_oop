import datetime
from typing import Set
from urllib.parse import urlparse, urljoin

import bs4
import requests


class URLTypeError(Exception):
    """Create instance of our own exception."""

    def __init__(self, msg: str = "Parameter 'url' is not string-like object."):
        super().__init__(msg)


class ScraperInitializer:
    """Create a session and return source html."""
    
    def __init__(self, url: str = ""):
        self.url = url
        
    @property
    def url(self) -> str:
        return self._url
    
    @url.setter
    def url(self, val: str):
        if not isinstance(val, str):
            raise URLTypeError()
        self._url = val
        
    def send_get_request(self) -> requests.models.Response:
        return requests.get(self.url)
    
    @staticmethod
    def parse_response(response):
        return bs4.BeautifulSoup(
            response.content,
            features="html.parser"
        )
    

class LinkProcessor:
    """Process the given soup object. Find the links and store them."""
    
    def __init__(self, url: str, soup: bs4.BeautifulSoup, keyword: str):
        self.url = url
        self.soup = soup
        self.keyword = keyword
        self.related_links: list = []
    
    def collect_all_links(self) -> Set[str]:   
        links = set()
        
        for link in self.soup.find_all("a"):
            if "href" in link.attrs and self.is_keyword(link.get("href")):
                links.add(
                    urljoin(self.url, link.get("href"))
                )
                
        return links

    def is_keyword(self, link: str) -> bool:
        return self.keyword in urlparse(link).path
    
    def create_link_object(self, links: Set[str]) -> None:
        """Create a new object 'LinkCollector' from the given links."""

        for link in links:
            self.related_links.append(
                LinkCollector(
                    path=urlparse(link).path,
                    scheme=urlparse(link).scheme,
                    netloc=urlparse(link).netloc,
                )
            )
        

class LinkCollector:
    """Create a new object from scheme, netloc, path and date."""
    fmt: str = "%d/%m/%y, %H:%M:%S"
    number_of_links: int = 0
    
    def __init__(self, path: str, scheme: str, netloc: str):
        self.path = path
        self.scheme = scheme
        self.netloc = netloc
        self.date = datetime.datetime.now().strftime(self.fmt)
        LinkCollector.increase_number_of_links()
        
    def __repr__(self) -> str:
        return str(f"{self.date}: {self.path[:45]}")
        
    @classmethod
    def increase_number_of_links(cls):
        cls.number_of_links += 1


# inicializovat objekt pro ziskani odpovedi
main_url: str = "https://engeto.cz"  # "https://www.idnes.cz"
app = ScraperInitializer()
# app.url = main_url
app.url = main_url

# zpracovat odkazy s hledanym klicovym slovem
links_idnes = LinkProcessor(
    main_url,
    app.parse_response(app.send_get_request()),
    "product",   # "zpravy"
)

# vytvorit prislusne objekty z novych hodnot
links_idnes.create_link_object(
    links_idnes.collect_all_links()
)