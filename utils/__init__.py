import logging
import datetime

logger = logging.getLogger('WebScrapper.scrapper.Scrapper')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler(f'{datetime.date.today()}.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)