 """
  By : Khaled ARARIA  
       PhD student at SBA
       Department of Electrical Engineering
      Faculty of Electrical Engineering
       Djillali Liabes University of Sidi Bel Abbes. 22000. Algeria.
       Laboratoire ICEPS (Intelligent Control & Electrical Power Systems)
       E-mail : kaled.araria@univ-sba.dz
"""
# - Exercice : 
#  Ecrire un programme python qui demande à saisir la longueur et la largeur d'un rectancle, calcule et affiche
#  son périmètre et sa surface.
#  Ecrire un programme python qui demande à saisir le rayon d'un circle, calcule et affiche son périmètre et sa
#  surface.
##################################################################
import math 
# ---------- Solution : Rectancle ------------#


longuer_rect=float(input("Entrez la valeur de la longueur du rectangle : A="))   # float()" convertir une chaîne de caractères (str) en un nombre à virgule flottante (float).
largeur_rect=float(input("Entrez la valeur de la largeur du rectangle : B="))
surface_rect=longuer_rect*largeur_rect
primetre_rect=(longuer_rect+largeur_rect)*2
print("Surface est S=AxB= {}".format(surface_rect))
print("Périmètre est P=(A+B)x2= {}".format(primetre_rect))

# ---------- Fin ------------#

# ---------- Solution : Circle------------#

rayon=float(input("Entrez du rayon d'un cercle  : r="))   # float()" convertir une chaîne de caractères (str) en un nombre à virgule flottante (float).
surface_c=math.pi*rayon**2
primetre_c=math.pi*rayon*2
print("Surface est S=3.14 x r²= {}".format(surface_c))
print("Périmètre est P=3.14 x 2r= {}".format(primetre_c))

# ---------- Fin ------------#
