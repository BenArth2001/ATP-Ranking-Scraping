from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrape_atp_rankings():
    url = 'https://www.atptour.com/en/rankings/singles'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    ranks = {}
    for row in soup.find_all('tr'):
        rank = row.find('td', class_='rank bold heavy tiny-cell')
        name_container = row.find('li', class_='name')
        age = row.find('td', class_='age')
        points = row.find('td', class_='points center bold extrabold small-cell')

        if rank and name_container and age and points:
            rank_text = rank.text.strip()
            name = name_container.find('span').text.strip()
            age_text = age.text.strip()
            points_text = points.text.strip()
            if rank_text.isdigit():
                ranks[int(rank_text)] = {'name': name, 'age': age_text, 'points': points_text}

    return ranks

@app.route('/get_player_by_rank')
def get_player_by_rank():
    rank = request.args.get('rank', default=1, type=int)
    players_data = scrape_atp_rankings()

    if rank in players_data:
        return jsonify(players_data[rank])
    else:
        return jsonify({'error': 'Player not found for the given rank'}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
