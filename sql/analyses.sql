-- A : Population moyenne par département

 SELECT d.nom,
	round(avg(c.population)) as  avg_population
 FROM communes c
 JOIN departements d
 ON c.code_departement = d.code
 GROUP BY d.nom
 ORDER BY avg_population DESC;


-- B : Départements dépassant 400 000 habitants

 SELECT d.nom,
	sum(c.population) as pop_dept
 FROM communes c
 JOIN departements d
 ON c.code_departement = d.code
 GROUP BY d.nom
 HAVING sum(c.population) > 400000;


-- C : Commune la plus peuplée par département

SELECT d.nom as departement,
       c.nom as commune,
       c.population
FROM communes c
JOIN departements d ON c.code_departement = d.code
WHERE c.population = (
    SELECT MAX(c2.population)
    FROM communes c2
    WHERE c2.code_departement = c.code_departement
);