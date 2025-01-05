'''Un nombre Rationnel est un quotient de deux entiers relatifs (un numérateur et un dénominateur).
Exemple : 2/7, 1/3
Ecrire les fonctions suivantes :
    • Saisie qui permet de saisir un quotient valide.
    • PGCD qui calcule du plus grand diviseur commun de deux nombres en utilisant la
méthode suivante :
    • Si A = B ; PGCD(A, B) = A
    • Si A>B ; PGCD(A, B) = PGCD(A-B, B)
    • Si A<B ; PGCD(A, B) = PGCD(A, B-A)
    Exemple : PGCD(18, 45) = PGCD(18, 27) = (PGCD(18, 9) = PGCD(9, 9) =9.
• Simplifie_R qui simplifie un nombre rationnel (on utilisera la fonction PGCD
    Exemple 12/8 = (12/PGCD(12,8))/(8/PGCD(12,8)) = (12/4)/(8/4) = 3/2
• Add_R qui additionne deux nombres rationnels et retourne un résultat simplifié
    Exemple : 5/4 + 1/5 = (5*5 +1*4)/(4 *5)= 29/20 = 13/10
• Ecrire un algorithme principal qui lit deux quotients et affiche leur somme'''

def saisie():
    while True:
        try:
            nb = int(input("Donner un entier: "))
            denom = int(input("Donner un dénominateur: "))
            if denom == 0:
                print("reessayer ")
                continue 
        except ValueError: 
            print("entrer un entier valide.")
        else:
            break
    return nb, denom

def PGCD(A,B):
    if(A==B):
        return A
    elif(A>B):
        return PGCD(A-B, B)
    else:
        return PGCD(A, B-A)
    
def Simplifie_R(nb1 , nb2):
    pgcd = PGCD(abs(nb1) , abs(nb2))
    return nb1 // pgcd , nb2 // pgcd

def Add_R(nb1,denom1, nb2, denom2):
    nb_result = nb1 * denom2 + nb2 * denom1
    denom_result = denom1 * denom2
    return Simplifie_R(nb_result,denom_result)

print("Entrez la première fraction :")
nb1, denom1 = saisie()
print("Entrez la deuxième fraction :")
nb2, denom2 = saisie()
nb, denom = Add_R(nb1, denom1, nb2, denom2)
print(Simplifie_R(nb, denom))