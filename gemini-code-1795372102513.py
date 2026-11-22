with open("index.html", "r", encoding="utf-8") as f:
    current_html = f.read()

print("Fichier index.html prêt à l'envoi, taille :", len(current_html), "octets")