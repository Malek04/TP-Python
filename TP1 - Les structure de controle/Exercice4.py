'''
L'utilisateur donne un entier supérieur à 1 et le programme affiche, s'il y en a, tous ses diviseurs propres
sans répétition ainsi que leur nombre. S'il n'y en a pas, il indique qu'il est premier
'''
def saisie():
    while True:
        try : 
            nb = int(input("donner un entier sup 1: "))
        except:
            print("reessayer")
        else:
            if(nb > 1):
                break
    return nb

n = saisie()
nb = 0
ch = ""
for i in range(2,n//2+1):
    if(n % i ==0):
        ch = ch + str(i) + " " 
        nb+=1
        
print(f"deviseur propre sans repition de {n} : {ch} (soit {nb} deviseur propre)")