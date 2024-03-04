from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Connexion à la BDD
DATABASE_URL = "mysql://root@db/ScrapingDB"
# DATABASE_URL = "mysql+pymysql://root@localhost:8889/ScrapingDB"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()