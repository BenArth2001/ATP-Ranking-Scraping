from sqlalchemy import Column, Integer, String, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.db import Base

# Ce fichier contient les classes SQLAlchemy qui 
# définissent vos tables. Chaque classe hérite de Base et 
# correspond à une table dans votre base de données. 

class Rank(Base):
    __tablename__ = 'rank'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    rank = Column(Integer, nullable=False)
    points = Column(Float, nullable=False)
