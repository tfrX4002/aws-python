with open("python.txt", "r") as fichier:
    contenu = fichier.read().replace("\n", " ")
print(contenu)