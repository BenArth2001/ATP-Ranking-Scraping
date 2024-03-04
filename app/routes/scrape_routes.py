from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.cruds.scrape_cruds import scrape_cruds

router = APIRouter()

@router.get("/get_data_ranks")
def get_data_ranks():
    cruds_scrape = scrape_cruds()
    try:
        return cruds_scrape.get_data_ranks()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des joueurs: {e}")

# @router.get("/rank/{nb_rank}")
# def get_rank(rank: int):
#     cruds_scrape = scrape_cruds()
#     try:
#         return cruds_scrape.get_rank(rank)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération de l'admin: {e}")