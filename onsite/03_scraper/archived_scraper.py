from urllib.parse import urlparse

import bs4
import requests


class LinkScraperInitializer:
    """Create session and return the bs4.BeautifulSoup object."""

    def send_get_request(self, host: str) -> requests.models.Response:
        return requests.get(host)

    def parse_html(self, response) -> bs4.BeautifulSoup:
        return bs4.BeautifulSoup(response.content, features="html.parser")


class LinkScraper:
    """Collects links of various types from a main url"""

    def __init__(self, soup: bs4.BeautifulSoup):
        self.soup = soup

    def collect_all_links(self) -> set:
        return {
            link.get("href")
            for link in self.soup.find_all("a")
            if "href" in link.attrs
        }


class LinkIterator:
    """Iterate through the given set of link."""

    def __init__(self, keyname: str, links: set):
        self.links = links
        self.keyname = keyname

    def iterate_through_links(self) -> set:
        """
        Iterate through the given set of links. Create 'parser' object
        that break the url up in comments and check the attr. 'path'.
        """
        result = set()
        
        for link in self.links:
            parser = ComponentParser(link, self.keyname)
            result.add(parser.add_verified_link())
        
        return result


class ComponentParser:
    """Break the url strings up in components."""

    def __init__(self, link: str, keyname: str):
        self.link = link
        self.keyname = keyname

    def parse_url(self):
        return urlparse(self.link)
    
    def is_path_correct(self, components) -> bool:
        return self.keyname in components.path
    
    def add_verified_link(self):
        if self.is_path_correct(self.parse_url()):
            return self.link


class Application:
    def run_scraper(self, host: str, keyword: str):
        # initiate the scraper
        runner = LinkScraperInitializer()
        parsed_html = runner.parse_html(runner.send_get_request(host))

        # collect the desirable links
        scraper = LinkScraper(parsed_html)
        links = scraper.collect_all_links()

        # iterate through the links
        iterator = LinkIterator(keyword, links)
        return iterator.iterate_through_links()


if __name__ == "__main__":
    app = Application()
    products = app.run_scraper("https://Engeto.cz", "product")
    news = app.run_scraper("https://idnes.cz", "zpravy")
    jobs = app.run_scraper("https://junior.guru/jobs", "jobs")
