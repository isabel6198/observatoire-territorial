
import requests
import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))  # ajoute src/ au path Python

from config import BRONZE, DB_PATH

# Configuration de la requete
DEPARTEMENT = input("Entrez le code du departement :") 
BASE_URL = "https://geo.api.gouv.fr"

# Chemin de sorti
output_path = BRONZE
output_file = output_path / f"communes_{DEPARTEMENT}.json"

# Construction de la requetes
url = f"{BASE_URL}/departements/{DEPARTEMENT}/communes"

params = {
    "fields": "nom,code,population"
}

# Appel de l'API pour récupérer les communes du département spécifié
response = requests.get(url, params=params)

# Traitement de la reponse
if response.status_code == 200:
    data = response.json()
    print(f"{len(data)} communes trouvees dans le departement {DEPARTEMENT}:\n")

    for commune in data:
        nom = commune.get("nom")
        code = commune.get("code")
        population = commune.get("population")
        print(f"Commune: {nom}, Code: {code}, Population: {population}")

        
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f" Les donnees ont ete enregistrees dans le fichier {output_file}\n")
    
else:    print(f"Erreur {response.status_code} lors de la requête" )

