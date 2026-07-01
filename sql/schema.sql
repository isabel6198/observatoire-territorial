
-- Table departement
CREATE TABLE IF NOT EXISTS departements (
    code     TEXT PRIMARY KEY,
    nom      TEXT NOT NULL
);

-- Table commune
CREATE TABLE IF NOT EXISTS communes (
    code      TEXT PRIMARY KEY,
    nom       TEXT NOT NULL,
    population  INTEGER ,
    code_departement TEXT,
    FOREIGN KEY (code_departement) REFERENCES departements(code)
);

-- creatio de la table indicateurs-departements 

CREATE TABLE IF NOT EXISTS  indicateurs_departements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code_departement TEXT NON NULL,
    annee INTEGER NOT NULL,
    taux_chomage REAL,
    revenu_median INTEGER,
    FOREIGN KEY (code_departement) REFERENCES departements(code)
);