from mappers.Mapper import Mapper
from models.Material_Front import Material_Front

class MaterialFrontMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_matirefront'
   
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(MaterialFrontMap._class_name)
        self.models = [Material_Front(name= str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']