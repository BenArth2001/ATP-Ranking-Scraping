from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from requests.exceptions import RequestException
from database.db import SessionLocal
from models.models import Ranking, Player
import pandas as pd
from bs4 import BeautifulSoup
from utils.DfToCsv import DfToCsv
import csv
import os


class db_cruds:
    """Classe pour les requetes bdd."""

    def save_datas_rank_db(self):
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

            # liste qui va contenir notre classement qu'on enregistrera dans un json
            rank_details = []
            try:
                for row in reader:
                    player = db.query(Player).filter(Player.name == row[1]).first()
                    if not player:
                        # Créez et ajoutez un nouveau joueur s'il n'existe pas
                        player = Player(name=row[1], age=int(row[2]))
                        db.add(player)
                        # Flush pour obtenir l'ID du joueur immédiatement
                        db.flush()  

                    # Ajoutez les informations du classement 
                    rank_details.append({
                        "id_p": player.id,
                        "Classement": int(row[0]),
                        "Points": float(row[3].replace(',', '.'))
                    })
                
                new_ranking = Ranking(rank_details=rank_details)
                db.add(new_ranking)
                db.commit()
            except Exception as e:
                db.rollback()
                print(f"Erreur lors de l'enregistrement des données : {e}")
                return None
            finally:
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
     