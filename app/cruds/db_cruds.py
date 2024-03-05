from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from requests.exceptions import RequestException
from database.db import SessionLocal
from models.models import Rank
import pandas as pd
from bs4 import BeautifulSoup
from utils.DfToCsv import DfToCsv
import csv
import os


class db_cruds:
    """Classe pour les requetes bdd."""

    def insert_datas_rank(self):
        # Recuperer le csv qui se trouve dans le dossier data_out
        current_script_path = os.path.abspath(__file__)
        app_directory = os.path.dirname(os.path.dirname(current_script_path))
        data_out_path = os.path.join(app_directory, 'data_out')
        
        db = SessionLocal()
        try:
            data_out_path = os.path.join(data_out_path, 'rank.csv')
        except Exception as e:
            print(f"Erreur lors de la récupération du fichier csv, le fichier est vide ou n'éxiste pas: {e}")
            return None
        
        with open(data_out_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            # next pour ignorer la première ligne (en tete du csv)
            next(reader)
            for row in reader:
                try:
                    rank_instance = Rank(
                        name=row[1],  
                        age=int(row[2]),  
                        rank=int(row[0]),  
                        points=float(row[3].replace(',', '.'))
                    )
                    db.add(rank_instance)
                    db.commit()

                except IntegrityError as e:
                    db.rollback()
                    print(f"Le joueur éxiste déjà: {row[1]}")
                except Exception as e:
                    print(f"Erreur inattendue: {e}")
        db.close()

        msg = "Les données ont été insérées avec succès."
        print(msg)
        return msg
        

    def get_player_by_rank(self, nb_rank: int):
        """On récupère les joueurs par rank."""
        db = SessionLocal()
        try:
            players = db.query(Rank).filter(Rank.rank == nb_rank).all()
            db.close()
            return players
        except SQLAlchemyError as e:
            db.rollback()
            print(f"Erreur lors de la récupération du joueur par rank: {e}")
            return None
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            return None
     