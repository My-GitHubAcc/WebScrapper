from mappers.Mapper import Mapper
from models.Gender import Gender

class GenderMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_gender'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(GenderMap._class_name)
        self.models = [Gender(name= str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']