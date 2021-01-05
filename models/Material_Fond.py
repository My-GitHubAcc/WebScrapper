from sqlalchemy import Column, String, Integer
from . import BaseModel
class Material_Fond(BaseModel):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, id, value):
        self.id = id
        self.name = value