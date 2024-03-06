from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import date

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(75), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    ranking_id = Column(Integer, ForeignKey('rankings.id'))

class Ranking(Base):
    __tablename__ = 'rankings'

    id = Column(Integer, primary_key=True, index=True)
    date_trait = Column(Date, default=date.today())
    rank_details = Column(JSON, nullable=False)

