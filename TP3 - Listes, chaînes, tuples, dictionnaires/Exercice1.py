#Soit la liste qui débute un script Python:
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
#Augmenter le script par les lignes de code qui répondent aux questions suivantes
#1. Ajouter la valeur 1 à chacun de ses éléments.
L = [element + 1 for element in L]
print(L)
#2. Ajouter les valeurs 11 et 12 à la fin de la liste.
L.append(11)
L.append(12)
#3. Afficher le premier élément, les deux premiers éléments, le dernier élément, les deux derniers éléments.
print(L[0])
print(L[:2])
print(L[-1])
print(L[-2:])
#4. Construire la liste Pairs qui contient les nombres paires de L et la liste Impairs qui contient les nombres "impaires" de L.
pair = [element for element in L if element % 2 ==0]
print(pair)
#5. Ajouter la valeur 3.5 entre 3 et 4.
L.insert(4,3.5)
print(L)
#6. Supprimer la valeur 3.5.
L.remove(3.5)
print(L)
#7. Inverser l'ordre des éléments de L.
L = L[::-1]
print(L)
#8. Demander à l'utilisateur de fournir un nombre au hasard et dire si ce nombre est présent dans L
while True:
    try:
        nb = int(input("saisie un entier: "))
    except:
        print("saisie un entier ")
    else:
        if(int(nb) == nb):
            break
if(nb in L):
    print(f"{nb} est un element de la liste")
else:
    print(f"{nb} n'est pas un element de la liste")