from sqlalchemy import Column, String, Integer
from . import BaseModel
class Taille_Lunettes(BaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, id, name):
        self.id = id
        self.name = name