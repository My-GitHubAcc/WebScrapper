from . import BaseModel
from sqlalchemy import Column, String, Integer
class Form(BaseModel):
    __tablename__ = "form"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    def __init__(self, id:int=None, name:str=None):
        self.id = id
        self.name = name
        