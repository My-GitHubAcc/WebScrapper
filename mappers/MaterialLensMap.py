from mappers.Mapper import Mapper
from models.Material_Lens import Material_Lens

class MaterialLensMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_matirelens'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(MaterialLensMap._class_name)
        self.models = [Material_Lens(name=str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']