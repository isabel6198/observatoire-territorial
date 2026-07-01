import sqlite3
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))  
from config import DB_PATH

SCHEMA_PATH = Path(__file__).parent.parent / "sql" / "schema.sql"  #   chemin absolu

schema = SCHEMA_PATH.read_text(encoding="utf-8")

connexion = sqlite3.connect(DB_PATH)
cursor = connexion.cursor()
cursor.executescript(schema)
connexion.commit()
connexion.close()

print("Base de données créée avec succès")