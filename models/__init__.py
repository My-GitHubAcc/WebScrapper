from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///db_demo.sqlite', echo=True)
db = sessionmaker(bind=engine)
BaseModel = declarative_base()