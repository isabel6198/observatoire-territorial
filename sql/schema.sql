
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
