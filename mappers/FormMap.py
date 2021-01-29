from mappers.Mapper import Mapper
from models.Form import Form

class FormMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_forme'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(FormMap._class_name)
        self.models = [Form(name= str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']