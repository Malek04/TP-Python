'''Ecrire un script Python qui déterminer si un nombre entier saisi au clavier est un nombre Parfait ou pas.
Principe : Un nombre égal à la somme de ses diviseurs propres est parfait.
Exemple : 6 Est Parfait car en effet 1, 2 et 3 sont les diviseurs propres de 6 et la somme de 1+2+3 = 6.'''

def saisie():
    while True:
        try:
            x = int(input("donner un entier: "))
        except:
            print("donner un entier ")
        else:
            if(x>0):
                break
    return x

x = saisie()
s = 0

for i in range(1,x//2+1):
    if(x % i ==0):
        s += i
if(s == x):
    print("c'est un diviseur propre")
else:
    print("non pas un diviseur propre")