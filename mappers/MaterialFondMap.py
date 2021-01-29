from mappers.Mapper import Mapper
from models.Material_Fond import Material_Fond

class MaterialFondMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_matirefond'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(MaterialFondMap._class_name)
        self.models = [Material_Fond(name=str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']