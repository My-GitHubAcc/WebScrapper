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
    material_fond_id = Column(Integer, ForeignKey('material_Fond.id'))
    material_front_id = Column(Integer, ForeignKey('material_Front.id'))
    structure_id = Column(Integer, ForeignKey('structure.id'))
    taille_lunettes_id = Column(Integer, ForeignKey('taille_lunettes.id'))
    taille_temple_id = Column(Integer, ForeignKey('taille_temple.id'))
    year = Column(String)

    def _init_(self, id, name, *,
                categorie_id:int=None, form_id:int=None, gender_id:int=None, marque_id:int=None, 
                material_fond_id:int=None, material_front_id:int=None, 
                structure_id:int=None, 
                taille_lunettes_id:int=None, taille_temple_id:int=None,
                year:str=None):
        self.id = id
        self.name = name
        self.categorie_id = categorie_id
        self.form_id = form_id
        self.gender_id = gender_id
        self.marque_id = marque_id
        self.material_fond_id = material_fond_id
        self.material_front_id = material_front_id
        self.structure_id = structure_id
        self.taille_lunettes_id = taille_lunettes_id
        self.taille_temple_id = taille_temple_id
        self.year = year