from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cruds.scrape_cruds import scrape_cruds
from fastapi.responses import FileResponse
import os

router = APIRouter()