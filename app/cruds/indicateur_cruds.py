from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from requests.exceptions import RequestException
from database.db import SessionLocal
from models.models import Ranking, Player
from sqlalchemy import func
from datetime import date
import datetime 
import pandas as pd
from bs4 import BeautifulSoup
from utils.DfToCsv import DfToCsv
import csv
import os


class indicateur_cruds:

    def get_sum_points_of_players(self):
        """Calculer la somme de tous les points des joueurs."""
        db = SessionLocal()
        try:
            last_ranking = db.query(Ranking).order_by(Ranking.date_trait.desc()).first()
            if last_ranking is None:
                print("Aucun classement n'a été trouvé.")
                return None
            
            rank_details = last_ranking.rank_details
            
            total_points = sum(player_data["Points"] for player_data in rank_details)
            
            return total_points
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Erreur lors du calcul de la somme des points : {e}")
            return None
        finally:
            db.close()

    def get_players_count(self):
        """Compter le nombre total de joueurs."""
        db = SessionLocal()
        try:
            player_count = db.query(func.count(Player.id)).scalar()
            return player_count
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Erreur lors du comptage des joueurs : {e}")
            return None
        finally:
            db.close()

    def get_min_player_age(self):
        """Trouver l'âge minimum parmi tous les joueurs."""
        db = SessionLocal()
        try:
            min_age = db.query(func.min(Player.age)).scalar()
            return min_age
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Erreur lors de la recherche de l'âge minimum : {e}")
            return None
        finally:
            db.close()

    def get_max_player_age(self):
        """Trouver l'âge maximum parmi tous les joueurs."""
        db = SessionLocal()
        try:
            max_age = db.query(func.max(Player.age)).scalar()
            return max_age
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Erreur lors de la recherche de l'âge maximum : {e}")
            return None
        finally:
            db.close()

    def get_avg_player_age(self):
        """Calculer l'âge moyen de tous les joueurs."""
        db = SessionLocal()
        try:
            avg_age = db.query(func.avg(Player.age)).scalar()
            return avg_age
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Erreur lors du calcul de l'âge moyen : {e}")
            return None
        finally:
            db.close()