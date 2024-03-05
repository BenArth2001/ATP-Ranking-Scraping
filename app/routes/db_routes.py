from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cruds.scrape_cruds import scrape_cruds

router = APIRouter()

@router.get("/insert_datas_rank")
def insert_datas_rank():
    cruds_scrape = scrape_cruds()
    try:
        csv_file_path = cruds_scrape.get_datas_rank()
        if "response" not in csv_file_path:
            return FileResponse(path=csv_file_path, filename="rank.csv", media_type='text/csv')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des classements des joueurs: {e}")
