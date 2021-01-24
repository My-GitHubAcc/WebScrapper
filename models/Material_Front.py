from sqlalchemy import Column, String, Integer
from . import BaseModel
class Material_Front(BaseModel):
    __tablename__ = "material_front"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    def __init__(self, id:int=None, name:str=None):
        self.id = id
        self.name = name