
from pathlib import Path


# Racine du projet
ROOT = Path(__file__).parent.parent

# Dossiers de stockage des donnees 
BRONZE = ROOT / "data" / "bronze"
SILVER = ROOT / "data" / "silver"
GOLD = ROOT / "data" / "gold"

# Base de donnees
DB_PATH = SILVER / "observatoire.db"



