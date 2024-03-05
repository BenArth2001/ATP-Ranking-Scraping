from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from requests.exceptions import RequestException
from database.db import SessionLocal
import requests
import pandas as pd
from bs4 import BeautifulSoup
from utils.DfToCsv import DfToCsv


class scrape_cruds:
    """Classe pour le scraping."""

    def scrape_atptour(self):
        """On se connecter au site."""

        base_url = 'https://www.atptour.com/en/rankings/singles'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }
        try:
            response = requests.get(base_url, headers=headers)
            response.raise_for_status()
        except RequestException as e:
            print(f"Erreur lors de la connexion au site: {e}")
            return None 

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    
    def get_datas_rank(self):
        """On récupere tous les rank scrapé."""

        datas_rank = []
        print("Récupération du classement...")
        soup = self.scrape_atptour()

        if soup:
            ranking_rows = soup.find_all('tr')
            for row in ranking_rows:
                try:
                    rank = row.find('td', class_='rank bold heavy tiny-cell')
                    name_container = row.find('li', class_='name')
                    age = row.find('td', class_='age')
                    points = row.find('td', class_='points center bold extrabold small-cell')

                    if rank and name_container and age and points:
                        player_name = name_container.find('span')
                        if player_name:
                            datas_rank.append({
                                'rank': rank.text.strip(),
                                'name': player_name.text.strip(),
                                'age': age.text.strip(),
                                'points': points.text.strip()
                            })
                except Exception as e:
                    print(f"Erreur lors du parsing des rank: {e}")
                    continue
        else:
            print("Aucune donnée à récupéré.")
        df_rank = pd.DataFrame(datas_rank) 
        df_to_csv = DfToCsv() 
        path_csv_rank = df_to_csv.register(df_rank, "rank.csv")

        return path_csv_rank