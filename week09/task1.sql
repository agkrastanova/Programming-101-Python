CREATE TABLE Languages(
  id INTEGER PRIMARY KEY,
  language VARCHAR(20),
  answer VARCHAR(50),
  answered INTEGER,
  giude TEXT
  );


INSERT INTO Languages
  VALUES(1, "Python", "google", 0, "A folder named Python was created. Go there and fight with program.py!")


INSERT INTO Languages
  VALUES(2, "Go", "200 OK", 0, "A folder named Go was created. Go there and try to make Google Go run."

INSERT INTO Languages
  VALUES(3,"Java","object oriented programming",0,"A folder named Java was created. Can you handle the class?")

INSERT INTO Languages
  VALUES(4,"Haskell", "Lambda",0,"Something pure has landed. Go to Haskell folder and see it!")

INSERT INTO Languages
  VALUES(5,"C#","NDI=",0,"Do you see sharp? Go to the C# folder and check out.")

INSERT INTO Languages
  VALUES(6,"Ruby","https://www.ruby-lang.org/bg/",0,"Ruby, ruby, rubyyy, aaahaaaahaa! (music). Go to Ruby folder!")

INSERT INTO Languages
  VALUES(7,"C++","header files",0,"Here be dragons! It's C++ time. Go to the C++ folder.")


ALTER TABLE Languages
  ADD rating INTEGER


UPDATE Languages
  SET rating=1
  WHERE id=1

UPDATE Languages
  SET rating=2
  WHERE id=2

UPDATE Languages
  SET rating=3
  WHERE id=3

UPDATE Languages
  SET rating=4
  WHERE id=4

UPDATE Languages
  SET rating=5
  WHERE id=5

UPDATE Languages
  SET rating=6
  WHERE id=6

UPDATE Languages
  SET rating=7
  WHERE id=7

UPDATE Languages
  SET rating=8
  WHERE id=8


UPDATE Languages
  SET answered=1
  WHERE language = "Python" OR language = "Go"

SELECT *
  FROM Languages
  WHERE answer = "200 OK" OR answer = "Lambda"

