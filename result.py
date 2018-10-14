"""Result page"""

import cgi
import cgitb
import chatons

cgitb.enable()
form = cgi.FieldStorage()

html_result = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title> Download images with Selenium</title
</head>
<body>
    <h1>Voici la page de l'application web de téléchargement d'images</h1>
    Merci, le téléchargement des images de 
</body>
</html>
"""

def printresult():
    print(str(html_result) + str(animal) + "s" + " est terminé!")

if form.getvalue("inputanimal"):
    animal = form.getvalue("inputanimal")
    chatons.getimages(animal)
    printresult()
else:
    raise Exception("Animal non écris")





