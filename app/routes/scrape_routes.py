from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cruds.scrape_cruds import scrape_cruds
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/get_datas_rank")
def get_datas_rank():
    cruds_scrape = scrape_cruds()
    try:
        csv_file_path = cruds_scrape.get_datas_rank()
        if csv_file_path is not None:
            return FileResponse(path=csv_file_path, filename='rank.csv', media_type='text/csv')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des rangs des joueurs: {e}")

# @router.get("/rank/{nb_rank}")
# def get_rank(rank: int):
#     cruds_scrape = scrape_cruds()
#     try:
#         return cruds_scrape.get_rank(rank)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération de l'admin: {e}")