import pandas as pd
import csv
import os

class DfToCsv:

    def register(self, dataframe, filename):

        try:
            # On récupère le chemin du fichier actuel
            current_script_path = os.path.abspath(__file__)
            app_directory = os.path.dirname(os.path.dirname(current_script_path))
            data_out_path = os.path.join(app_directory, 'data_out')
            os.makedirs(data_out_path, exist_ok=True)
            file_path = os.path.join(data_out_path, filename)

            try:
                dataframe.to_csv(file_path, index=False)
                print("Le csv a été enregistré avec succès.")
            except Exception as e:
                print(f"Une erreur s'est produite lors de l'enregistrement du dataframe : {str(e)}")
                return None
            
        except Exception as e:
            print(f"Une erreur s'est produite lors de l'enregistrement du dataframe : {str(e)}")
            return None
        
        return file_path
