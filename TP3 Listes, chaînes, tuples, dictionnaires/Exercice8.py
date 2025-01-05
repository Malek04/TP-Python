'''Soient les deux listes suivantes titres et infos qui contiennent respectivement les titres des
livres et les informations relatives à ces livres:
Titres = ["Témoin muet', 'Germinal', 'Le roi Lear', 'Candide', '1984']
Infos = [['Christie', 17.8, 17], ['Zola', 52, 12], ['Shakespeare', 27, 23], ['Voltaire', 35.5, 30], ['Orwell', 25, 15]]
Chaque élément de la liste Infos est une liste qui contient le nom de l'auteur du livre, le prix en DT (Dinar Tunisien)
et le nombre de copies disponibles.
La liste des Achats contient le liste des livres achetés par un client.
Les éléments de la liste sont des tuples dont chacun contient le nom d'un livre et le nombre de copies achetées.
Achats = [('Candide', 2), ('Germinal', 1), (*1984', 4]
Travail demandé:'''
# 1. Écrire la fonction Librairie(Titres, Infos) permettant de retourner le dictionnaire D. 
# Pour notre exemple, la fonction Librairie(Titres, Infos) retourne le dictionnaire suivant: 
# {"Témoin muet": ['Christie', 17.8, 17], 'Germinal': ['Zola', 52, 12], 'Le roi Lear': ['Shakespeare', 27, 23], 
# 'Candide': ['Voltaire', 35.5, 30], '1984': ['Orwell', 25, 15]}
def Librairie(Titres, Infos):
    D = {Titres[i]: Infos[i] for i in range(len(Titres))}
    return D

# 2. Écrire la fonction RecherchePrix(D, prix) qui permet de retourner la liste des titres des livres du dictionnaire D 
# dont le prix est inférieur ou égal à prix (prix est un réel).
def RecherchePrix(D, prix):
    livres = [titre for titre, infos in D.items() if infos[1] <= prix]
    return livres

# 3. Écrire la fonction Montant(D, Achats) qui étant donné le dictionnaire D et la liste des achats d'un client 
# retourne le montant que ce client doit payer.
def Montant(D, Achats):
    total = 0
    for achat in Achats:
        titre, copies = achat
        total += D[titre][1] * copies
    return total

# 4. Écrire la fonction Actualisation(D, Achats) qui permet de mettre à jour le nombre de copies de livres du dictionnaire D 
# après les achats effectués par un client. Si après cette mise à jour, le nombre de copies d'un livre est égal à 0, 
# alors on supprime ce livre du dictionnaire D.
def Actualisation(D, Achats):
    for achat in Achats:
        titre, copies = achat
        D[titre][2] -= copies
        if D[titre][2] == 0:
            del D[titre]
    return D

# 5. Programme principal qui permet de:
#    Créer le dictionnaire D, puis l'afficher.
#    Afficher la liste des livres dont le prix est inférieur ou égal à 25 DT.
#    Calculer et afficher le montant à payer en achetant les livres indiqués dans la liste des Achats.
#    Mettre à jour le dictionnaire D suite aux achats indiqués dans la liste Achats.

Titres = ["Témoin muet", "Germinal", "Le roi Lear", "Candide", "1984"]
Infos = [['Christie', 17.8, 17], ['Zola', 52, 12], ['Shakespeare', 27, 23], ['Voltaire', 35.5, 30], ['Orwell', 25, 15]]
Achats = [('Candide', 2), ('Germinal', 1), ('1984', 4)]

D = Librairie(Titres, Infos)

print("Dictionnaire des livres :")
print(D)

livres_pour_prix = RecherchePrix(D, 25)
print("Livres dont le prix est inférieur ou égal à 25 DT :")
print(livres_pour_prix)

montant_a_payer = Montant(D, Achats)
print("Montant à payer :")
print(montant_a_payer, "DT")

D_Actualise = Actualisation(D, Achats)
print("Dictionnaire après les achats (copies mises à jour) :")
print(D_Actualise)
