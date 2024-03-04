from scraper import scrape_and_save_to_csv, get_player_by_rank
from api import app

def main():
    scrape_and_save_to_csv()

    while True:
        rank = input("Entrez le classement du joueur que vous souhaitez obtenir (ou 'q' pour quitter) : ")
        if rank.lower() == 'q':
            break
        try:
            rank = int(rank)
            player_data = get_player_by_rank(rank)
            if player_data:
                print(f"Données du joueur avec le classement {rank}:")
                print(player_data)
            else:
                print(f"Joueur non trouvé pour le classement {rank}")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")

if __name__ == "__main__":
    main()
