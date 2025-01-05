'''Soit L une liste de nombres entiers donnés.
Soit n un entier donné par l'utilisateur.
1. Ecrire une procédure listeEntiers() qui permet de créer une liste d'entiers positifs.
2. Ecrire une fonction verif(n,L) : qui vérifie si n appartient à la liste L ou non.
3. Ecrire un script qui vérifie si n est un élément de L et calculer l'effectif et la fréquence de n
dans cette liste ; sinon il affiche un message d'erreur.
Par exemple, si L = [0,10,20,10,20,30,20,30,40,20], et n = 20 alors son effectif est 4 (nombre de fois
où il apparaît) et sa fréquence est 4/10 (effectif de la valeur / effectif total).'''
def saisie():
    while True:
        try :
            nb = int(input("donner un entier "))
        except:
            print("donner un entier")
        else:
            if(int(nb) == nb):
                break
    return nb

def listeEntiers():
    L = []
    continuer = 'O'
    while(continuer.upper() == 'O'):
        nb = saisie()
        L.append(nb)
        continuer = input("Voulez vous continuer O/N ? ")
    return L

def verif(n,L):
    if(n in L):
        return True
    else:
        return False
    
L = listeEntiers()
n = saisie()
effectif = 0
frequence = 0
if(verif(n,L)):
    for element in L:
        if(element == n):
            effectif+=1
    frequence = effectif / len(L)
    print(f"l'effectif {effectif} la frequence {frequence}")
else:
    print("Erreur")