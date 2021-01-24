from . import BaseModel
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.schema import ForeignKey
class Lunettes(BaseModel):
    __tablename__ = "lunettes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    categorie_id = Column(Integer, ForeignKey('categorie.id'))
    form_id = Column(Integer, ForeignKey('form.id'))
    gender_id = Column(Integer, ForeignKey('gender.id'))
    marque_id = Column(Integer, ForeignKey('marque.id'))
    material_Fond_id = Column(Integer, ForeignKey('material_Fond.id'))
    material_Front_id = Column(Integer, ForeignKey('material_Front.id'))
    material_lens_id = Column(Integer, ForeignKey('material_lens.id'))
    structure_id = Column(Integer, ForeignKey('structure.id'))
    taille_lunettes_id = Column(Integer, ForeignKey('taille_lunettes.id'))
    taille_temple_id = Column(Integer, ForeignKey('taille_temple.id'))

    def _init_(self, id, name:str, 
                categorie:int=None, form:int=None, gender:int=None, marque:int=None, 
                material_fond:int=None, material_front:int=None, material_lens:int=None, 
                structure:int=None, 
                taille_lunettes:int=None, taille_temple:int=None):
        self.id = id
        self.name = name
        self.categorie_id = categorie
        self.form_id = form
        self.gender_id = gender
        self.marque_id = marque
        self.material_Fond_id = material_fond
        self.material_Front_id = material_front
        self.material_lens_id = material_lens
        self.structure_id = structure
        self.taille_lunettes_id = taille_lunettes
        self.taille_temple_id = taille_temple