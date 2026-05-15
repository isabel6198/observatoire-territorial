
import requests
import json
from pathlib import  Path

# Configuration de la requete
DEPARTEMENT = [ "09", "11", "12", "30", "31", "32", "34", "46", "48", "65",  "66", "81", "82" ]
BASE_URL = "https://geo.api.gouv.fr"

# Chemin de sorti
output_path = Path("data/raw")

# Construction de la requetes

params = {
    "fields": "nom,code,population,departement"
}

total_communes = 0
total_departements = 0

# Appel de l'API pour récupérer les communes du département spécifié

for dept in DEPARTEMENT:
    url = f"{BASE_URL}/departements/{dept}/communes"
    response = requests.get(url, params=params)
    output_file = output_path / f"communes_{dept}.json"

    
    # Traitement de la reponse
    if response.status_code == 200:
        data = response.json()
        print(f"{len(data)} communes trouvees dans le departement {dept}:\n")
        print(f" Departement: {dept} sauvargerdes : \n")

        for commune in data:
            nom = commune.get("nom")
            code = commune.get("code")
            population = commune.get("population")
            print(f"Commune: {nom}, Code: {code}, Population: {population}")

            
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f" Les donnees ont ete enregistrees dans le fichier {output_file}\n")
        total_communes += len(data)
        total_departements += 1
        
    else:    print(f"Erreur {response.status_code} lors de la requête" )

print(f" Total communes :  {total_communes} dans {total_departements} departements")
