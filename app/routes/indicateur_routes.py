from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from cruds.indicateur_cruds import indicateur_cruds
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/get_sum_points_of_players")
def get_sum_points_of_players():
    cruds_indicateur = indicateur_cruds()
    try:
        sum_age = cruds_indicateur.get_sum_points_of_players()
        return {"message": sum_age}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du calcul de la somme des âges : {e}")
    
@router.get("/get_players_count")
def get_players_count():
    cruds_indicateur = indicateur_cruds()
    try:
        player_count = cruds_indicateur.get_players_count()
        return {"message": player_count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du comptage des joueurs : {e}")
    
@router.get("/get_min_player_age")
def get_min_player_age():
    cruds_indicateur = indicateur_cruds()
    try:
        min_age = cruds_indicateur.get_min_player_age()
        return {"message": min_age}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la recherche de l'âge minimum : {e}")
    
@router.get("/get_max_player_age")
def get_max_player_age():
    cruds_indicateur = indicateur_cruds()
    try:
        max_age = cruds_indicateur.get_max_player_age()
        return {"message": max_age}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la recherche de l'âge maximum : {e}")
    
@router.get("/get_avg_player_age")
def get_avg_player_age():
    cruds_indicateur = indicateur_cruds()
    try:
        avg_age = cruds_indicateur.get_avg_player_age()
        return {"message": avg_age}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du calcul de l'âge moyen : {e}")
    

    