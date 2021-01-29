from mappers.Mapper import Mapper
from models.Taille_Temple import Taille_Temple

class TailleTempleMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_tailletemple'
    
    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(self._class_name)
        self.models = [Taille_Temple(name=str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']