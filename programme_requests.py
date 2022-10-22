import fileinput

import requests

reponse = requests.get("https://www.currentschoolnews.com/wp-content/uploads/2022/06/naruto.jpg")
file = open("papillon.jpg", "wb")
file.write(reponse.content)
file.close()
