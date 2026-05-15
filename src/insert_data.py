
import sqlite3
import json
from pathlib import Path


# chemins
DB_PATH = Path("data/processed/observatoire.db")
RAW_PATH = Path("data/raw")

connexion = sqlite3.connect(DB_PATH)
cursor = connexion.cursor()

total_communes = 0


# Parcours de fichiers JSON dans le dossier raw
for json_file in RAW_PATH.glob("communes_*.json"):
    data = json.loads(json_file.read_text(encoding="utf-8"))
# Insertion des donnes dans la base de donnees

    if not data:
        continue
    
    premier = data[0]
    dept_code = premier["departement"]["code"]
    nom_dept = premier["departement"]["nom"]


    cursor.execute("""
                INSERT OR IGNORE INTO departements (code, nom)
                VALUES (?, ?)
                """, (dept_code, nom_dept))

    for commune in data:
        cursor.execute("""
                    INSERT OR IGNORE INTO communes (code, nom, population, code_departement)
                    VALUES (?, ?, ?, ?)
                    """, (commune["code"], commune["nom"], commune["population"], dept_code)
                    )
        total_communes += 1

connexion.commit()
connexion.close()

print (f" ingestion terminee pour :{total_communes} communes ")

