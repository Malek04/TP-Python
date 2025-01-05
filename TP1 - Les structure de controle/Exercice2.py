'''Écrivez un programme pour saisir un numéro de l'utilisateur et échangez le premier et le dernier chiffre
du numéro donné.
    Exemple :
    Saisir un nombre : 1987
    Après l'échange : 7981'''

def saisie():
    while True:
        try : 
            nb = int(input("donner un entier "))
        except:
            print("donner un entier ")
        else:
            if(nb > 0):
                break
    return nb

nombre = saisie()

ch = str(nombre)
ch1 = ch[-1] + ch[1:-1] + ch[0]

nombre = int(ch1)
print(nombre)