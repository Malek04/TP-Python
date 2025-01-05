'''
Le but de cet exercice est de calculer la somme des achats d'un client puis d'afficher cette somme après remise.
La remise est calculée en fonction de la somme et selon la formule suivante :
    • Pour une somme inférieure é 50 DT, la remise est de 3%
    • Pour une somme entre 50 DT et I00 DT, la remise est de 5%
    • Pour une somme dépassant 100 DT, la remise est de 7%
Ecrire un programme python qui permet de :
    - Saisir P le prix d'un article (réel strictement positif)
    - Calculer S la somme des prix
    - Demander à l'utilisateur s'il veut ajouter un autre article à son panier. Sa réponse rep prend la
valeur « O » pour « Oui » ou « N » pour « Non ».
Ces trois instructions seront répétées autant de fois jusqu'à ce que la réponse de l'utilisateur soit « N »
(arrêt).
    - Calculer puis afficher la somme finale SF après remise.'''

def controle():
    while True : 
        try:
            article = int(input("prix article: "))
        except:
            print("prix article: ")
        else:
            if(article>0):
                break
    return article

def achat():
    s = controle()
    print("voulez vous ajouter un article?")
    ajout = input("O/N: ")
    while(ajout.upper()=='O'):
        s += controle()
        print("voulez vous ajouter un article?")
        ajout = input("O/N: ")
    return s

def prix_remise(achat):
    if(achat<50):
        remise = achat - (achat/100)*3
    elif (achat > 50 and achat <100):
        remise = achat - (achat/100)*5
    else:
        remise = achat - (achat/100)*7
    return remise

total = achat()
SF = prix_remise(total)
print(f"le prix est {total} apres remise est {SF}")