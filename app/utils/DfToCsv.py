import pandas as pd
import os
from pathlib import Path

class DfToCsv:

    def register(self, dataframe, filename):
        root_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(root_directory, 'data_out', filename)
        
        # S'assurer que le dossier 'data_out' existe
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        try:
            dataframe.to_csv(file_path, mode="w", header=False, index=False)
            print("Le csv a été enregistré avec succès.")
        except Exception as e:
            return{"message": f"Une erreur s'est produite lors de l'enregistrement du dataframe : {str(e)}"}
        return file_path