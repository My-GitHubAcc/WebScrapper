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

    def _init_(self, id, name):
        self.id = id
        self.name = name