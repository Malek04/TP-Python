#Ecrire des fonctions permettant de :
#1. Saisir un entier supérieur à 2 puis saisit et retourne les données de n étudiants (nom,
#note cc et note examen) dans 3 listes

L_nom = []
L_noteCC = []
L_noteEx = []
L_Moy = []

def saisie():
    while True:
        try:
            nb = int(input("donner un entier superieur a 2 "))
        except:
            print("reesayer")
        else:
            if(nb > 2):
                break
    return nb

n = saisie()

def saisie_note():
    while True:
        try:
            note = int(input("donner un note "))
        except:
            print("donner une note ")
        else:
            if(0 <= note <= 20):
                break
    return note

def Add_student():
    global L_nom, L_noteCC, L_noteEx
    for _ in range(n):
        nom = input("nom d'etudiant")
        note_cc = saisie_note()
        note_ex = saisie_note()
        L_nom.append(nom)
        L_noteCC.append(note_cc)
        L_noteEx.append(note_ex)

# 2. Crée et retourne une liste contenant les moyennes de tous les étudiants (moyenne = note cc*0.3+ note examen*0.7)
def Moy():
    global L_noteCC, L_noteEx, L_Moy
    for i in range(len(L_noteCC)):
        moy = L_noteCC[i] * 0.3 + L_noteEx[i] * 0.7
        L_Moy.append(round(moy, 2))
    return L_Moy

# 3. Affiche pour chaque étudiant sa moyenne
def Moy_Etud():
    global L_Moy
    for nom, moy in zip(L_nom, L_Moy):
        print(f"l'etudiant {nom} a {moy}")

# 4. Trie les trois listes par ordre croissant de moyenne
def trier_par_moyenne():
    global L_nom, L_noteCC, L_noteEx
    moyennes = Moy()
    etudiants = list(zip(L_nom, L_noteCC, L_noteEx, moyennes))
    etudiants_tries = sorted(etudiants, key=lambda x: x[3], reverse=True)
    L_nom, L_noteCC, L_noteEx = zip(*[(nom, cc, ex) for nom, cc, ex, moy in etudiants_tries])
    return list(L_nom), list(L_noteCC), list(L_noteEx)

# 5. Crée puis affiche et retourne une liste de listes avec les noms, moyennes et rang de tous les étudiants
def creer_liste_rangs():
    global L_nom, L_noteCC, L_noteEx, L_Moy
    moyennes = Moy()
    etudiants_rangs = [(nom, moy) for nom, moy in zip(L_nom, moyennes)]
    etudiants_rangs = sorted(etudiants_rangs, key=lambda x: x[1])
    rangs = []
    for i, (nom, moy) in enumerate(etudiants_rangs, 1):
        rangs.append([nom, moy, i])
    return rangs

# 6. Transfert du contenu de la liste créée dans une liste de dictionnaires
def convertir_en_dictionnaires():
    global L_nom, L_noteCC, L_noteEx, L_Moy
    rangs = creer_liste_rangs()
    dictionnaires = []
    for nom, moy, rang in rangs:
        idx = L_nom.index(nom)
        note_cc = L_noteCC[idx]
        note_ex = L_noteEx[idx]
        dictionnaire = {
            "nom": nom,
            "resultat": (note_cc, note_ex, moy, rang)
        }
        dictionnaires.append(dictionnaire)
    dictionnaires.sort(key=lambda x: x['resultat'][2])
    return dictionnaires

# 7. Ajouter un nouvel étudiant tout en maintenant la liste triée par moyenne
def ajouter_nouvel_etudiant():
    global L_nom, L_noteCC, L_noteEx
    nom = input("Nom de l'étudiant à ajouter : ")
    note_cc = saisie_note()
    note_ex = saisie_note()
    L_nom.append(nom)
    L_noteCC.append(note_cc)
    L_noteEx.append(note_ex)
    trier_par_moyenne()

#Programme principale
Add_student()  
Moy_Etud()  
L_nom, L_noteCC, L_noteEx = trier_par_moyenne()
creer_liste_rangs()
dictionnaires = convertir_en_dictionnaires()
ajouter_nouvel_etudiant()

# Affichage après ajout d'un nouvel étudiant
print("Ajout Etudiant")
Moy_Etud()

# Affichage des rangs
print("Affichage des rangs")
rangs = creer_liste_rangs()
for rang in rangs:
    print(f"{rang[0]} : Moyenne = {rang[1]} , Rang = {rang[2]}")

# Affichage des dictionnaires
print("Affichage des dictionnaires")
dictionnaires = convertir_en_dictionnaires()
for dic in dictionnaires:
    print(dic)
