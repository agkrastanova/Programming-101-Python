SELECT address
  FROM STUDIO
  WHERE name="MGM"


SELECT birthdate
  FROM MOVIESTAR
  WHERE name="Kim Basinger"


SELECT name
  FROM MOVIEEXEC
  WHERE networth>10000000


SELECT name
  FROM MOVIESTAR
  WHERE gender="M" OR address="Prefect Rd"


INSERT INTO MOVIESTAR
 VALUES ("Zahari Baharov", "Sofiyska 1", "M", "1990-08-12");


DELETE FROM STUDIO
  WHERE address LIKE "%5%"


UPDATE MOVIE
  SET studioname="Fox"
  WHERE title LIKE "%star%"



-- Relations


SELECT starname
  FROM STARSIN
  JOIN MOVIESTAR on STARSIN.starname = MOVIESTAR.name
  WHERE STARSIN.movietitle="Terms of Endearment" AND MOVIESTAR.gender="M"


SELECT starname
  FROM STARSIN
  JOIN MOVIE on MOVIE.TITLE = STARSIN.MOVIETITLE
  JOIN STUDIO ON STUDIO.name = MOVIE.STUDIONAME
  WHERE STARSIN.movieyear=1995 AND MOVIE.studioname="MGM"


ALTER TABLE STUDIO
  ADD COLUMN president_cert INTEGER REFERENCES MOVIEEXEC(cert)


UPDATE STUDIO
  SET president_cert=123
  WHERE STUDIO.name="MGM"


UPDATE STUDIO
  SET president_cert=199
  WHERE STUDIO.name="USA Entertainm."


SELECT MOVIEEXEC.name
  FROM MOVIEEXEC
  JOIn STUDIO ON STUDIO.pres_cert = MOVIEEXEC.cert
  WHERE STUDIO.name="MGM"

