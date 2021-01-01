import requests
from bs4 import BeautifulSoup
from requests.models import Response

class Scrapper:
    def getPage(_, url) -> Response:
        response = None
        try:
            response = requests.get(url)
        except ValueError:
            pass
        return response
    
    def getContent(self, url) :
        self.soup = BeautifulSoup(self.getPage(url).content, 'html.parser')

    def getElementById(self, id):
        return self.soup.find(id=id)

    def getElementsByClass(self, className):
        return self.soup.find_all(class_=className)

    def getElementsBySelectors(self, selectors):
        return self.soup.find_all(attrs=selectors)
