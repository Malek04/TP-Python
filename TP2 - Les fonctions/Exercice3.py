'''Écrire une fonction qui permet de lire et retourner un nombre compris entre 2 et 9.
2) Écrire une fonction vérifier (n, b) qui étant donné un nombre n et une base b (b est comprise
entre 2 et 9) retourne vrai si n appartient à b et faux sinon.
3) Écrire une fonction convertir (n, b) qui convertit un nombre de la base b en décimal et
retourne le résultat.
4) Écrire un programme qui :
- lit un nombre positif n et une base b.
- Si n n'appartient pas à b, il affiche un message d'erreur, sinon elle le convertit en décimal et
affiche le résultat.
- Demander à l'utilisateur s'il veut effectuer une autre conversion. Sa réponse rep prend la
valeur « O » pour « Oui » ou « N » pour « Non ».
- Ces trois instructions seront répétées autant de fois jusqu'à ce que la réponse de
l'utilisateur soit « N » (arrêt)'''
def verif():
    while True:
        try: 
            nb = int(input("donner un entier positif: "))
        except : 
            print("donner un entier positif")
        else:
            if(nb > 1):
                break
    return nb

def saisie():
    while True:
        try: 
            nb = int(input("donner un entier entre 2 et 9: "))
        except : 
            print("donner un entier entre 2 et 9")
        else:
            if(nb >= 2 and nb <= 9):
                break
    return nb

def verifier(n,b):
    for chiffre in str(n):
        if(int(chiffre))>=b:
            return False
    return True

def convertir (n, b):
    n = str(n)[::-1]
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (b ** i)
    return result

continuer = 'O'
while(continuer.upper() =='O'):
    n = verif()
    b = saisie()
    if(not verifier(n,b)):
        print(f"Le nombre {n} n'est pas en base {b}")
        continuer = input("voulez vous continuer O/N ?")
    else:
        chiffre = convertir(n,b)
        print(f"le nombre {n} en base {b} est {chiffre}")
        continuer = input("voulez vous continuer O/N ?")
