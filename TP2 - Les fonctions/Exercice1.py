'''
Ecrire un programme python permettant de déterminer le nombre de chiffres constituant un entier
saisi au clavier.
'''

def saisie():
    while True:
        try:
            nb = int(input("donner un entier "))
        except:
            print("donner un entier")
        else:
            break
    return nb

def chiffrement(n):
    return len(str(abs(n)))
    
nb = saisie()
size = chiffrement(nb)

print(f"le nombre {nb} contient {size} chiffre")