SELECT c.name AS Categorie,
       f.name AS Forme,
       g.name AS Gender,
       m.name AS Marque,
       mf.name AS [Material Fond],
       mfr.name AS [Material Front],
       s.name AS Structure,
       t.name AS Taille,
       tt.name AS [Taille Temple],
       l.year
  FROM lunettes AS l
       JOIN
       categorie AS c ON c.id = l.categorie_id
       JOIN
       form AS f ON f.id = l.form_id
       JOIN
       gender AS g ON g.id = l.gender_id
       JOIN
       marque AS m ON m.id = l.marque_id
       JOIN
       material_fond AS mf ON mf.id = l.material_fond_id
       JOIN
       material_front AS mfr ON mfr.id = l.material_front_id
       JOIN
       structure AS s ON s.id = l.structure_id
       JOIN
       taille_lunettes AS t ON t.id = l.taille_lunettes_id
       JOIN
       taille_temple AS tt ON tt.id = l.taille_temple_id;
