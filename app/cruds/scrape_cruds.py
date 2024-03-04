from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from requests.exceptions import RequestException
from database.db import SessionLocal
import requests
from bs4 import BeautifulSoup

class scrape_cruds:
    """Classe pour les players."""
    def scrape_atptour():
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
    
    def get_data_ranks(soup):
        """Récupère tous les ranks."""
        datas_ranks = []

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
                            datas_ranks.append({
                                'rank': rank.text.strip(),
                                'name': player_name.text.strip(),
                                'age': age.text.strip(),
                                'points': points.text.strip()
                            })
                except Exception as e:
                    print(f"Erreur lors du parsing des ranks: {e}")
                    continue
        else:
            print("Aucune donnée à récupéré.")
        return datas_ranks