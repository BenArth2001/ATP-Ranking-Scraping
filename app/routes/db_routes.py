from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.cruds.scrape_cruds import scrape_cruds

router = APIRouter()