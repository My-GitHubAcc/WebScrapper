import requests
from bs4 import BeautifulSoup
from requests.models import Response
import logging

class Scrapper:
    def __init__(self, url: str):
        self.logger = logging.getLogger('WebScrapper.scrapper.Scrapper')
        self.logger.info(f'Scrapper instance created with url={url}')
        self._getContent(url)

    def _getPage(self, url: str) -> Response:
        """
            Launch a GET request to a designated url\n
            Return the HTML page from the request
        """
        response = None
        try:
            response = requests.get(url)
        except ConnectionError as error:
            self.logger.error(f"{error.filename} => {error.strerror}")
        return response

    def _getContent(self, url: str) :
        """
            Parse an HTML page into a BeautifulSoup object
        """
        try:
            self.soup = BeautifulSoup(self._getPage(url).content, 'html.parser')
        except (AttributeError, KeyError) as error:
            self.logger.error(f"{error.filename} => {error.strerror}")
        

    def getElementById(self, id: str):
        """
            Get HTML element by the given id inside the page
        """
        if self.soup is None: 
            raise ValueError("Page not loaded properly")

        element = self.soup.find(id=id)
        self.logger.debug(f'Fetched elements: {element.name} with id: {id}')
        return element

    def getElementsByClass(self, className: str):
        """
            Get HTML element by the given class inside the page
        """
        if self.soup is None: 
            raise ValueError("Page not loaded properly")
        elements = self.soup.find_all(class_=className)
        self.logger.debug(f'Fetched elements with className: {className}')
        return elements

    def getElementsBySelectors(self, selectors):
        """
            Get HTML element by the given attribute values inside the page
        """
        if self.soup is None: 
            raise ValueError("Page not loaded properly")
        elements =self.soup.find_all(attrs=selectors)
        self.logger.debug(f'Fetched elements with attributes: {selectors}')
        return elements
