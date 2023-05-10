 """
  By : Khaled ARARIA  
       PhD student at SBA
       Department of Electrical Engineering
      Faculty of Electrical Engineering
       Djillali Liabes University of Sidi Bel Abbes. 22000. Algeria.
       Laboratoire ICEPS (Intelligent Control & Electrical Power Systems)
       E-mail : kaled.araria@univ-sba.dz
"""
  
# - Exercice :  Les conditions
#  Ecrire un programme python qui demande à saisir deux nombre et affiche le maximum des deux.

##################################################################

# ---------- Solution : Rectancle ------------#


valeur_1=float(input("Entrez le 1er valeur : valeur_1="))   # float()" convertir une chaîne de caractères (str) en un nombre à virgule flottante (float).
valeur_2=float(input("Entrez le 2eme valeur : valeur_2="))   # float()" convertir une chaîne de caractères (str) en un nombre à virgule flottante (float).
if valeur_1 > valeur_2:
  print("Le nombre maximum est : {}".format(valeur_1))
else:
    print("Le nombre maximum est : {}".format(valeur_2))

    

# ---------- Fin ------------#  
