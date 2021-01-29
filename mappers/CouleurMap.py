from mappers.Mapper import Mapper
from models.Couleur import Couleur

class CouleurMap(Mapper):
    #_tag = 'select'
    _class_name = 'woof_container_inner_couleur'

    def mapModels(self, url:str):
        self.loadPage(url)
        parentElement = self.scrapper.getElementsByClass(self._class_name)
        self.models = [Couleur(name=el.get('value'))
                for el in parentElement[0].descendants 
                if el.name == 'input']
