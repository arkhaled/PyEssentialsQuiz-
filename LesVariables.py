# - Exercice : 
#  Ecrire un programme python qui demande à saisir la longueur et la largeur d'un rectancle, calcule et affiche
#  son périmètre et sa surface.
#  Ecrire un programme python qui demande à saisir le rayon d'un circle, calcule et affiche son périmètre et sa
#  surface.
##################################################################

# ---------- Solution ------------#


longuer_rect=float(input("Entrez la valeur de la longueur du rectangle : A="))   # float()" convertir une chaîne de caractères (str) en un nombre à virgule flottante (float).
largeur_rect=float(input("Entrez la valeur de la largeur du rectangle : B="))
surface=longuer_rect*largeur_rect
Primetre=(longuer_rect+largeur_rect)*2
print("Surface est S=AxB= {}".format(surface))
print("Périmètre est P=(A+B)x2= {}".format(Primetre))

