
import requests


# Configuration de la requete
DEPARTEMENT = "34"
BASE_URL = "https://geo.api.gouv.fr"

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
    
else:    print("Erreur{response.status_code} lors de la requête" )

