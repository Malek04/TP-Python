'''On appelle mot de Dyck tout mot construit à partir de deux lettres lettre1 et lettre2 
verifiant les deux propriétés suivantes:
-Le mot doit commencer par lettre1 et contenir autant de la lettre1 que de la lettre2
-Dans tout prefixe du mot, le nombre d'occurences de lettre1 est superieur ou egal au nombre
 d'occurences de lettre2, c'est a dire lorsqu'on fait le parcours du mot du gauche a droite 
 on a toujour le nombre_lettre1 >= nombre_lettre2
Exemples: Pour lettre1='F' et lettre2='B':
-Le mot 'FBFB' est un mot DYCK car dans tous ses prefixes qui sont 'F', 'FB', 'FBF' et 'FBFB' 
on a nombre_lettre1 >= nombre_lettre2
-Le mot 'FFBF' n'est pas un mot DYCK car nombre_lettre1 > nombre_lettre2
-Le mot 'FBBF' n'est pas un mot DYCK car dans le prefixe 'FBB' on a nombre_lettre2 > nombre_lettre2
On veut tester si un mot donné est un mot de DYCK en verifiant le principe decrit ci-dessus,
Pour cela on cherche à écrire les trois fonctions suivantes:
1. La fonction Occurence(m, lettre1) qui calcule et retourne le nombre d'occurences d'une lettre lettre1 dans le mot m
2. La fonction MotAdeux(m) qui vérifie si le mot m donné en paramètre est formé de suelement deux letrtes 
à nombres d'occurences égaux Si c'est le cas la fonction retourne les deux letrtes en question dans une liste, sinon elle retourne False
NB. Cette fonction fait appel aux à la fonction Occurence déjà définie
3. La fonction Est_Dyck(m) qui vérifie si le mot m donné en paramètre est un mot de Dyck ou non.
La fonction affiche le résultat de la vérification
NB.Cette fonction fait appel aux deux fonctions précédemment définies
'''
def Occurence(m , lettre1):
    nb = 0
    for c in m:
        if (c == lettre1):
            nb += 1
    return nb

def MotAdeux(m):
    l = set(m) 
    if len(l) == 2:
        lettre1, lettre2 = list(l)
        if Occurence(m, lettre1) == Occurence(m, lettre2):
            return [lettre1, lettre2]
    return False

def Est_Dyck(m):
    l = MotAdeux(m)
    if not l:
        return False
    
    lettre1, lettre2 = l[0], l[1]

    if m[0] != lettre1:
        return False    
    
    if Occurence(m, lettre1) != Occurence(m, lettre2):
        return False
    
    l1 = 0
    l2 = 0
    for char in m:
        if char == lettre1:
            l1 += 1
        else:
            l2 += 1
        if l2 > l1:
            return False
        
    return True

ch = str(input("Donner une chaîne de caractères: "))
print(Est_Dyck(ch))
