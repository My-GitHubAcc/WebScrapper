import logging
from sqlalchemy.orm.session import Session
from utils.scrapper import Scrapper
import concurrent.futures
class Mapper:
    def __init__(self):
        # self.scrapper = Scrapper(url)
        self.logger = logging.getLogger('WebScrapper.mappers.Mapper')
    
    def mapModels(_):
        pass
    
    def saveToDb(self, engine):
        session = Session(bind = engine)
        session.add_all(self.models)
        session.commit()

    def loadPage(self, url):
        self.logger.debug(f'Loading page: {url}')
        with concurrent.futures.ThreadPoolExecutor() as executor:
            f = executor.submit(Scrapper, url)
            self.scrapper = f.result()