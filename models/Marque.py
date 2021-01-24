from sqlalchemy import Column, String, Integer
from . import BaseModel
class Marque(BaseModel):
    __tablename__ = "marque"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    def __init__(self, id:int=None, name:str=None):
        self.id = id
        self.name = name