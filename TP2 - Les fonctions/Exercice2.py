'''Ecrire une fonction saisie() qui permet de retourner un entier saisi au clavier composé de 3 chiffres au maximum
Ecrire une fonction chiffrePorteBonheur(nb) qui permet de déterminer si un nombre entier nb est  chiffre porte Bonheur ou non.
Un nombre chiffre porte Bonheur est un nombre entier qui, lorsqu'on ajoute les carrés de chacun de
ses chiffres, puis les carrés des chiffres de ce résultat et ainsi de suite jusqu'à l'obtention d'un
nombre à un seul chiffre égal à 1 (un).
Le calcule s'arrête lorsque le chiffre devient inférieur à 10'''

def saisie():
    while True:
        try:
            nb = int(input("donner un entier de trois chiffre au maximum: "))
        except:
            print("ressayer")
        else:
            if(nb>0 and nb<1000):
                break
    return nb

def chiffrePorteBonheur(nb):
    while nb != 1 and nb >= 10:
        s = 0
        for n in str(nb):
            s += int(n) ** 2 
        nb = s 
    return nb == 1  

nb = saisie()
result = chiffrePorteBonheur(nb)
if(result == True):
    print(f"le chiffre {nb} est un porte bonheur")
else:
    print(f"le chiffre {nb} n'est pas un porte bonheur")