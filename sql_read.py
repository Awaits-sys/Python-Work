import sqlite3

connexion = sqlite3.connect("Albums.db")
curseur = connexion.cursor()

curseur.execute("SELECT nom FROM artiste")
artistes = curseur.fetchall()

album_cd = curseur.execute("SELECT titre FROM album a JOIN artiste b ON a.artiste_id = b.artiste_id AND b.nom = \"CELINE DION\"").fetchall()
print(album_cd)

connexion.close()
