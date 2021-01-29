from mappers.Mapper import Mapper
from models.Categorie import Categorie

class CategorieMap(Mapper):
    #_tag = 'ul'
    _class_name = 'woof_container_inner_catgorie'

    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(self._class_name)
        self.models = [Categorie(name=str(el.find(text=True))) 
                for el in parentElement[0].ul.descendants 
                if el.name == 'label']
