from mappers.Mapper import Mapper
from models.Structure import Structure

class StructureMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_structure'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(StructureMap._class_name)
        self.models = [Structure(name= str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']