from typing import List
from fastapi import FastAPI
from database.db import engine
from models.models import Base
from routes import scrape_routes
from routes import db_routes
from routes import indicateur_routes

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(scrape_routes.router, prefix="/scrape", tags=["scrape"])
app.include_router(db_routes.router, prefix="/database", tags=["database"])
app.include_router(db_routes.router, prefix="/indicateur", tags=["indicateur"])
