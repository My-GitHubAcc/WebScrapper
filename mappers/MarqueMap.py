from mappers.Mapper import Mapper
from models.Marque import Marque

class MarqueMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_marque'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(MarqueMap._class_name)
        self.models = [Marque(name=str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']