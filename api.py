from flask import Flask, jsonify, request
from scraper import scrape_and_save_to_csv, get_player_by_rank

app = Flask(__name__)

@app.route('/get_player_by_rank')
def get_player():
    rank = request.args.get('rank', default=1, type=int)
    scrape_and_save_to_csv()  # Appel à la fonction de scraping
    player_data = get_player_by_rank(rank)
    return jsonify(player_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
