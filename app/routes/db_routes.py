from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cruds.db_cruds import db_cruds

router = APIRouter()

@router.get("/insert_rank")
def insert_datas_rank():
    cruds_db = db_cruds()
    try:
        insert_db = cruds_db.insert_datas_rank()
        return {"message": insert_db}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Veuillez récupéré le classement avant de l'inserer en base de donnée: {e}")

@router.post("/get_player_by_rank/{nb_rank}")
def get_rank(nb_rank: int):
    cruds_db = db_cruds()
    try:
        player_data = cruds_db.get_player_by_rank(nb_rank)
        return {"message": player_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération du joueurs par le classement: {e}")