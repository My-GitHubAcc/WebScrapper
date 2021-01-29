from mappers.Mapper import Mapper
from models.Taille_Lunettes import Taille_Lunettes

class TailleLunettesMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_taille'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(self._class_name)
        self.models = [Taille_Lunettes(name=el.get('value')) 
                for el in parentElement[0].descendants 
                if el.name == 'input']