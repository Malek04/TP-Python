'''On cherche à évaluer la force des mots de passe des différents utilisateurs d'un site web.
Un mot de passe est une chaine de caractères qui ne comporte pas d'espaces.
La force d'un mot de passe varie, scion la valeur d'un Score calcule, de « Très faible » jusqu'à
« Très fort » :
➢ Si le score <20, la force du mot de passe est « Très faible »
➢ Sinon si le score<40, la force d'un mot de passe est « Faible »
➢ Sinon si le score <80, la force du mot de passe est « Fort »
➢ Sinon la force du mot de passe est « Très Fort »
Le score se calcule en additionnant des bonus et en retranchant des pénalités.
Les bonus attribués sont : • Nombre total de caractères * 4
• (Nombre total de caractères - nombre des lettres majuscules) * 2
• (Nombre total de caractères - nombre des lettres minuscules) * 3
• Nombre de caractères non alphabétiques * 5
Les pénalités imposées sont : • La longueur de la plus longue séquence de lettres minuscules * 2
• La longueur de la plus longue séquence de lettres majuscules * 3
Exemple :
Pour le mot de passe « P@cSI_promo2017 », le score se calcule comme suit :
La somme de bonus = 15*4 + (15-3) *2 + (15-6) *3+6*5=141
• Le nombre total de caractères = 15
• Le nombre de lettres majuscules = 3
• Le nombre de lettres minuscules=6
• Le nombre de caractères non alphabétiques =6
La somme des pénalités = 5*2+2*3=16
•La longueur de la plus longue séquence de lettres minuscules ('promo')
=5
•La longueur de la plus longue séquence de lettres majuscules ('SI') =Le score final = 141-
16=125 ; puisque I25>80 alors le mot de passe est considéré comme
« Très fort »'''
#1- Ecrire les fonctions suivantes :
#a. nbMin qui calcule le nombre des caractères minuscules d’une chaîne
def nbMin(ch):
    nb = 0
    for c in ch:
        if(c>='a' and c<='z'):
            nb += 1
    return nb

#b. nbMax qui calcule le nombre des caractères majuscules d’une chaîne
def nbMax(ch):
    nb = 0
    for c in ch:
        if(c>='A' and c<='Z'):
            nb += 1
    return nb

#c. nbNonAlpha qui calcule le nombre des caractères non alphabétiques d’une chaîne
def nbNonAlpha(ch):
    nb = 0
    for c in ch:
        if(not(c>='A' and c<='Z') and not(c>='a' and c<='z')):
            nb += 1
    return nb

#d. LongMaj qui calcule la longueur de la plus longue séquence de lettres majuscules dans une chaîne
def LongMaj(chaine):
    max_len = 0 
    current_len = 0
    for char in chaine:
        if char.isupper():
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len

#e. LongMin qui calcule la longueur de la plus longue séquence de lettres minuscules dans une chaîne
def LongMin(chaine):
    max_len = 0 
    current_len = 0
    for char in chaine:
        if char.islower():
            current_len += 1
            max_len = max(max_len, current_len)
        else:
            current_len = 0
    return max_len

#2- Ecrire un script Python permettant de :
# Saisir une chaine correspondante au mot de passe
# Vérifier si la chaine ne contient pas des espaces, si la chaine contient des espaces on doit les supprimer.
# Calculer la somme des bonus, la somme des pénalités et le score de mot de
#passe sachant que :
#le score= la somme des bonus — la somme des pénalités.
# Afficher la force du mot de passe saisi scion la valeur du score

mdp = input("donner un mot de passe")
mdp = mdp.replace(" ","")
nb_total_caracteres = len(mdp)
nb_maj = nbMax(mdp)
nb_min = nbMin(mdp)
nb_non_alpha = nbNonAlpha(mdp)

bonus = (
    nb_total_caracteres * 4 +
    (nb_total_caracteres - nb_maj) * 2 +
    (nb_total_caracteres - nb_min) * 3 +
    nb_non_alpha * 5
)

longueurs_sequence_min = LongMin(mdp)
longueurs_sequence_maj = LongMaj(mdp)
penalites = (longueurs_sequence_min * 2 +longueurs_sequence_maj * 3)
score = bonus - penalites

if score < 20:
    force = "Très faible"
elif score < 40:
    force = "Faible"
elif score < 80:
    force = "Fort"
else:
    force = "Très fort"
print(force)