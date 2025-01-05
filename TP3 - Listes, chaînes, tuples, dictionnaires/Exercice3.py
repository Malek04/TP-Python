from random import *
#On considère les deux listes suivantes :
Couleurs = ['Pique','Cœur','Carreau','Trefle']
Valeurs = ['7','8','9','10','Valet','Reine','Roi','As']
#1. Écrire un script qui affiche toutes les cartes d’un jeu de 32 cartes
for couleur in reversed(Couleurs):
    for val in Valeurs:
        print(f"{val} de {couleur}",end=" ")
    print("")
'''2. Écrire un script qui renvoie une liste de N cartes prises au hasard dans le jeu. Par exemple,
avec N = 2, on devrait pouvoir obtenir [As de Trèfle, Dix de Pique].
Une première approche est de choisir n fois une valeur et une couleur dans les listes
correspondantes avec la fonction choice(liste).'''
L = []
for i in range(randint(0,10)):
    color = choice(Couleurs)
    val = choice(Valeurs)
    carte = f"{val} de {color}"
    L.append(carte)
print(L)
'''Modifier le script précédent pour éviter d'avoir deux cartes identiques. Avant d'ajouter une
nouvelle carte, on vérifie que l'élément n'est pas déjà présent dans la liste.'''
L = []
for i in range(randint(1,10)):
    color = choice(Couleurs)
    val = choice(Valeurs)
    carte = f"{val} de {color}"
    while(carte in L):
        color = choice(Couleurs)
        val = choice(Valeurs)
        carte = f"{val} de {color}"
    L.append(carte)
print(L)
