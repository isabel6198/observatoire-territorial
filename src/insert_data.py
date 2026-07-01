import sqlite3
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
from config import BRONZE, DB_PATH

connexion = sqlite3.connect(DB_PATH)
cursor = connexion.cursor()

total_communes = 0

for json_file in BRONZE.glob("communes_*.json"):
    data = json.loads(json_file.read_text(encoding="utf-8"))

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
        """, (commune["code"], commune["nom"], commune["population"], dept_code))
        total_communes += 1

connexion.commit()
connexion.close()

print(f"Ingestion terminée : {total_communes} communes")