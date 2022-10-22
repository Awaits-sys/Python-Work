import sqlite3

connexion = sqlite3.connect("Albums.db")
curseur = connexion.cursor()

curseur.execute("CREATE TABLE artiste (artiste_id INTEGER NOT NULL PRIMARY KEY, nom VARCHAR);")
curseur.execute("CREATE TABLE album (album_id INTEGER NOT NULL PRIMARY KEY, artiste_id INTEGER REFERENCES artiste, titre VARCHAR, annee_sortie INTEGER)")

curseur.execute("INSERT INTO artiste (nom) VALUES (\"Michael Jackson\");")
mj_id = curseur.lastrowid
curseur.execute("INSERT INTO artiste (nom) VALUES (\"Céline Dion\");")
cd_id = curseur.lastrowid

curseur.execute(f"INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({mj_id}, \"Thriller\", 1983);")
curseur.execute(f"INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({cd_id}, \"Falling into you\",1996);")
curseur.execute(f"INSERT INTO album (artiste_id, titre, annee_sortie) VALUES ({cd_id}, \"Let's talk about love\", 1997);")

connexion.commit()
connexion.close()