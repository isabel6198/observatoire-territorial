
import sqlite3
from pathlib import Path

# Chemins
DB_PATH = Path("data/processed/observatoire.db")
SCHEMA_PATH = Path("sql/schema.sql")

# lecture du schema
schema = SCHEMA_PATH.read_text(encoding="utf-8")


# connexion et acreation

connexion = sqlite3.connect(DB_PATH)
cursor = connexion.cursor()
cursor.executescript(schema)
connexion.commit()
connexion.close()

print ("Base de donnes cree avec succes")
