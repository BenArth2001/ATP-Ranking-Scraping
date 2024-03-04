import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, ranks):
    ranking_rows = soup.find_all('tr')

    for row in ranking_rows:
        rank = row.find('td', class_='rank bold heavy tiny-cell')
        name_container = row.find('li', class_='name')
        age = row.find('td', class_='age')
        points = row.find('td', class_='points center bold extrabold small-cell')

        if rank and name_container and age and points:
            ranks.append({
                'rank': rank.text.strip(),
                'name': name_container.find('span').text.strip(),
                'age': age.text.strip(),
                'points': points.text.strip()
            })

def scrape_atp_rankings():
    base_url = 'https://www.atptour.com/en/rankings/singles'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    page = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    ranks = []
    scrape_page(soup, ranks)
    return ranks

def scrape_and_save_to_csv():
    ranks = scrape_atp_rankings()
    with open('ranking.csv', 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Rank', 'Name', 'Age', 'Points'])

        for player in ranks:
            writer.writerow([player['rank'], player['name'], player['age'], player['points']])

def get_player_by_rank(rank):
    players_data = {}
    with open('ranking.csv', 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if int(row['Rank']) == rank:
                players_data = {
                    'rank': row['Rank'],
                    'name': row['Name'],
                    'age': row['Age'],
                    'points': row['Points']
                }
                break
    return players_data
