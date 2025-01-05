'''
L'adresse IPV4 est un numéro servant à identifier d'une façon unique chaque ordinateur
connecté au réseau d'internet. Elle a la forme suivante : W.X.Y.Z avec W, X, Y et Z sont
quatre entiers positifs compris entre 0 et 255 (par exemple : 155.105.50.69 est une IPV4).
On se propose dans cette partie de vérifier la validité des adresses IPV4 stockées en
tant que chaines de caractères dans une liste L (par exemple :
L=['155.105.50.69',' 155.105.50.47','155.105.50.58','155.105.50.61'])
Pour vérifier la validité d'une adresse IPV4, il suffit de vérifier que la chaine de caractères,
qui la représente, est formée par quatre sous-chaines W, X, Y et Z dont la conversion
de chacune enun entier appartient à l'intervalle [0, 255].
Indications :
La fonction ch. split (sep) permet de retourner la liste formée par les sous-chaines de
la chainede caractères ch séparées par le caractère sep donné en argument (par
exemple '155.105.50.69'. split('.') donne la liste [' 155', '105', '50', '69' ]).
La fonction ch. isdigit () renvoie True si la chaine de caractères ch n'est formée
que par des caractères numériques, False, sinon.
Travail demandé :'''
#1. Ecrire la fonction booléenne testVal (v) qui renvoie la valeur True si
# l'entier v appartient à l'intervalle [0, 255], False, sinon.
def testVal(v):
    return 0 <= v <= 255
#2. Ecrire la fonction booléenne valide (ip) qui permet de vérifier la validité d'une
#adresse IPV4 (le paramètre ip est une chaine de caractères représentant l'adresse IPV4).
def valide(ip):
    adresse = ip.split('.')
    if len(adresse) != 4:
        return False
    for ad in adresse:
        if (not ad.isdigit()):
            return False
        value = int(ad)
        if (not testVal(value)):
            return False
    return True
#3. Ecrire la fonction récursive validiP (l) qui renvoie une liste ne contenant que les adresses IPV4 valides.
def ValidIp(l):
    if not l:
        return []
    if(valide(l[0])):
        return [l[0]] + ValidIp(l[1:])
    else:
        return ValidIp(l[1:])
'''
Partie 2
Chaque adresse IPV4 valide appartient à l'une des classes suivantes :
- Classe A, si la valeur du premier bit à gauche de la représentation en binaire de W est 0.
- Classe B, si la valeur des deux premiers bits à gauche de la représentation en binaire
de W est10.
- Classe C, si la valeur des trois premiers bits à gauche de la représentation en binaire
de W est110.
- Classe D, si la valeur des quatre premiers bits à gauche de la représentation en
binaire de West 1110.
- Classe E, si la valeur des quatre premiers bits à gauche de la représentation en
binaire de West 1111.
Exemple :
L'adresse 155.105.50.69 est valide et elle appartient à la classe B car la valeur des
deuxpremiers bits à gauche de la représentation en binaire de 155 qui est 10011011 est
10.
Indication :
La fonction bin (nb) permet de convertir en binaire un nombre décimal nb (par
exemple : bin(155) retourne la chaine de caractères ' Ob10011011 ' )
Travail demandé :
'''
#4. Ecrire la fonction binaire (n) qui retourne la représentation binaire de n sans le
#préfixe '0b'.
def binaire(n):
    return bin(n)[2:]
#5. Ecrire la fonction classe (ip) qui retourne la chaine de caractères représentant la classe
#d'une adresse ip donnée en paramètre.
def classe (ip):
    premierbit = int(ip.split('.')[0])
    if binaire(premierbit)[0] == '0':
        return "A"
    if binaire(premierbit)[0:2] == '10':
        return "B"
    if binaire(premierbit)[0:3] == '110':
        return "C"
    if binaire(premierbit)[0:4] == '1110':
        return "D"
    if binaire(premierbit)[0:] == '1111':
        return "E"
#6. Ecrire la fonction creerList (l) qui reçoit en argument la liste l contenant des adresses
#IPV4 et retourne la liste des tuples dont chacun est formé par une adresse IPV4 valide
#ainsi quela classe à laquelle elle appartient (Exemple de tuple dans la liste retournée :
#('155.105.50.69', 'B' )).
def creerList(l):
    liste_tuple =[]
    for element in l:
        if(valide(element)):
            liste_tuple.append((element,classe(element)))
    return liste_tuple
#7. Ecrire la fonction récursive nbClass (l, ch) permettant de compter le nombre
#d'adresses dans la liste des tuples l, passée en premier argument, qui appartiennent à la
#classe ch passée en deuxième argument.
def nbClass(l, ch):
    if not l:
        return 0
    else:
        if l[0][1] == ch:
            return 1 + nbClass(l[1:], ch)
        else:
            return nbClass(l[1:], ch)
#8. Ecrire la fonction creerDict (l) permettant de retourner le dictionnaire dont les clés
#sont toutes les classes des adresses ('A', 'B', 'E') et leurs valeurs correspondantes
#sont leurs nombres d'occurrences dans la liste des tuples l donnée en argument.
def creerDict(l):
    classes = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0} 
    for adresse, cls in l:
        if cls in classes:
            classes[cls] += 1
    return classes
#9. Ecrire un script python permettant de :
#▪ Saisir un ensemble d'adresses IP par l'utilisateur
print("Entrez des adresses IP")
adresses = input().split()
# Afficher la liste des adresses IP valides
print("Adresses IP valides:")
valides = ValidIp(adresses)
print(valides)
# Créer et afficher la liste des adresses IP valides et leurs classes
print("Liste des adresses IP valides et leurs classes:")
adresses_et_classes = creerList(adresses) 
print(adresses_et_classes)
# Créer et afficher un dictionnaire contenant le nombre des adresses de chaque classe
print("Dictionnaire des occurrences de chaque classe:")
dictionnaire_classes = creerDict(adresses_et_classes)
print(dictionnaire_classes)