from random import *
'''
1) Créer un programme pour simuler un jeu entre un joueur et l'ordinateur selon les règles suivantes :
- Le joueur sélectionne un nombre entre 1 et 5, représentant le nombre de doigts étendus.
- L'ordinateur choisit également un nombre aléatoire entre 1 et 5.
Si la somme des deux nombres est paire, le joueur remporte la partie ; sinon, c'est l'ordinateur qui
gagne.
2) Suggérer une méthode permettant au programme d'offrir, à la fin de chaque partie, l'option de
rejouer. Si l'utilisateur choisit « non », le programme devra afficher le nom du gagnant.
'''
def saisie():
    while True:
        try:
            nb = int(input("donner un entier entre 1 et 5"))
        except:
            print("Reessayer")
        else:
            if(nb>=1 and nb<=5):
                break
    return nb

continuer = 'O'
while(continuer.upper() == 'O'):
    user = saisie()
    ordinateur=randint(1,5)
    if(user + ordinateur % 2 == 0 ):
        print("Vous avez gagner")
    else:
        print("Vous avez perdu")
    continuer = input("Voulez vous continuer O/N? ")