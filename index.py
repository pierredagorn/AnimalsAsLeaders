"""Homepage for the program"""

print("Content-type : text/html; charset=utf-8\n")

html_accueil = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title> Download images with Selenium</title
</head>
<body>
    <h1>Voici la page de l'application web de téléchargement d'image</h1>
    <p>Cette application en python va chercher des images sur intermouette!</p>
</body>
</html>
"""

html_form = """
<!DOCTYPE html>
<html>
<body>
<h2>Quel est ton animal favori dans un dico d'animaux!! ?</h2>
    <form action="/result.py" method="post">
    <p><input name="inputanimal" type="text">
    <input type="submit"></p>
</form>
</body>
</html>
"""

print(html_accueil)
print(html_form)

