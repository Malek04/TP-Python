'''Organisation des jeux olympique
Les organisateurs desjeux olympiquessouhaitent informatiser la gestion de cet évènement. Dans
ce sujet on s’intéresse en particulier aux épreuves et à la gestion de leurs résultats.
Les jeux Olympiques réunissent des athlètes issus de nombreux pays.
Les athlètes sont identifiés par leur nom, leur prénom, âge et le pays pour lequel ils concourent.
Chaque athlète est un objet de classe Athlète
A. Partiel :
Écrire la classe Athlète qui possède les méthodes suivantes :'''

class Athlete:
    #1. Un constructeur : qui permet de définir les attributs de chaque athlète.
    def __init__(self, nom, prenom, age, pays):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.pays = pays
    #2. str : la méthode spéciale qui permet d’afficher toutes les informations concernant l'athlète selon le fomat suivant:
    #« l’athlète Oussama Mallouli âgé de 27 ans vient de Tunisie »
    def __str__(self):
        return f"l'athlète {self.nom} {self.prenom} âgé de {self.age} ans vient de {self.pays}"
    #3. peg :laméthode spécialequitestesideuxathlètesontlemême âge,c’estlaméthode qui
    #permet detester l’égalité dedeux objets Athlètes (==).
    def __peg__(self, other):
        if isinstance(other, Athlete):
            return self.age == other.age
        return False
'''B. Partie 2 :
Les résultats des athlètes sont représentés par des objets de type Résultat.
Chaque résultat a une nature et une épreuve concernée, Chaque nature du
résultat change suivant l'épreuve et peutse mesurer :
- Par un temps, c'est le cas des épreuves de course vitesse, marathon et natation.
- Par une distance, c'est le cas des épreuves de lances etsauts.
- Par un nombre de points, c'est le cas des épreuves de plongeon, en tire et
décathlon.
Afin de catégoriser les épreuves selon la nature on crée trois listes Lt, Ld et Lnb stockant
les épreuves de même nature, respectivement temps distance et nombre de points.
Ecrire la classe Résultat, possédant :'''
class Resultat:
    #1. Trois (3) attributs de classes Lt, Ld et Lnb,
    Lt = [] 
    Ld = []
    Lnb = [] 
    #2. Un constructeur définissant le nom de l’épreuve nomE ainsi que la nature natR initialement vide.
    def __init__(self, nomE):
        self.nomE = nomE 
        self.natR = "" 
    #3. Une méthode Set_nature permettant de fixer la nature du résultat selon l’épreuve concerné.
    # Cette nature est une chaine de caractère parmi ‘temps’, ’distance’ et ’nombre de points’.
    def Set_nature(self, nature):
        if nature not in ['temps', 'distance', 'nombre de points']:
            print("Erreur : La nature doit être 'temps', 'distance' ou 'nombre de points'.")
        else:
            self.natR = nature
    #4. Une méthode Comparable qui teste si deux objets Résultat ont une même nature ou non.
    def __peg__(self, other):
        if isinstance(other, Resultat):
            return self.natR == other.natR
        return False
    #5. Une méthode spéciale repr permettant d’afficher l’épreuve et sa nature comme l’exemple suivant :
    #« Le résultat de l’épreuve de course_vitesse se mesure par un temps »
    def __repr__(self):
        return f"Le résultat de l'épreuve de {self.nomE} se mesure par un {self.natR}"
'''
C. Partie 3 :
Les résultats des athlètes sont répartis par la suite en 3 types afin de spécifier la valeur du
résultat obtenu qui doit être compatible avec sa nature, c'est à dire on va créer par la suite :
➢ La classe RésultatTemps pour l'objet résultat caractérisé par le temps effectué
par un athlète dans une épreuve. Le temps est une valeur entière.
➢ La classe Résultatdistance pour l'objet résultat caractérisé par la distance
réalisée par un athlète dans une épreuve. La distance est une valeur réelle.
➢ La classe RésultatNbpoints pour l'objet résultat caractérisé par le nombre de
points calculés pour un athlète dans une épreuve. Le nombre de points est une
valeur entière.
Chacune des 3 classes hérite la classe Résultat et y ajoute :
- Un attribut public valeur qui représente la valeur du résultat de l'athlète initialement nulle.
- Une méthode Set_val permettant de saisir la valeur du résultat selon la nature de l'épreuve.
- Une méthode spéciale repr permettant d'afficher toutes les informations concernant le résultat.'''
#1. Ecrire la classe RésultatTemps.
class ResultatTemps(Resultat):
    def __init__(self, nomE):
        super().__init__(nomE)
        self.valeur = None

    def Set_val(self, valeur):
        if isinstance(valeur, int):
            self.valeur = valeur
        else:
            print("Erreur : La valeur du temps doit être un entier.")
    def __repr__(self):
        return f"{super().__repr__()} avec un temps de {self.valeur} secondes."
#2. Ecrire la classe Résultatdistance.
class ResultatDistance(Resultat):
    def __init__(self, nomE):
        super().__init__(nomE)
        self.valeur = None 
    def Set_val(self, valeur):
        if isinstance(valeur, float):
            self.valeur = valeur
        else:
            print("Erreur : La valeur de la distance doit être un nombre réel.")
    def __repr__(self):
        return f"{super().__repr__()} avec une distance de {self.valeur} mètres."
#3. Ecrire la classe RésultntNbpoints. (Proposer une solution pour cette classe avec un autre méthode d’héritage)
class ResultatNbpoints(Resultat):
    def __init__(self, nomE):
        super().__init__(nomE)
        self.valeur = None 
    def Set_val(self, valeur):
        if isinstance(valeur, int):
            self.valeur = valeur
        else:
            print("Erreur : La valeur des points doit être un entier.")
    def __repr__(self):
        return f"{super().__repr__()} avec {self.valeur} points."
'''
D. Partie 4 :
Les épreuves sont modélisées pars des instances de la classe Epreuve.
Ces objets permettent de gérer les informations concernant les athlètes participant à l’épreuve
et leur résultat à celle-ci. Ces informations sont stockées dans un dictionnaire nommé DEprev
dont :
- Les clés sont des objets Athlètes
- Les valeurs sont des objets Resultats suivant la nature du résultat. C'est-à-dire des objets
RésultatTemps, Résultatdistance et RésultntNbpoints.

Chaque épreuve à un record mondial que les athlètes eassayent de le battre.
Chaque gagnant de l'épreuve, celui qui a obtenu une valeur maximale des résultats aura une
médaille d'or.'''
#Ecrire la classe Epreuve contenant :
#1. Un constructeur définissant :
#▪ NomE un attribut public représentant le nom de l’épreuve
#▪ DEprv un attribut privé de type dictionnaire initialement vide.
#▪ Nbrecord un attribut public calculant le nombre de records battus dans cette épreuve initialement null.
class Epreuve:
    def __init__(self, nomE):
        self.nomE = nomE
        self._DEprev = {}
        self.Nbrecord = 0
    #2. Une méthode AjoutAthlète permettant d’ajouter un athlète inexistant à l’épreuve.
    #Remarque : affecter une valeur None pour un ajout d’athlète sans résultat
    def AjoutAthlète(self, athlète, resultat=None):
        if athlète not in self._DEprev:
            self._DEprev[athlète] = resultat
        else:
            print(f"{athlète.nom} {athlète.prenom} est déjà inscrit à l'épreuve.")
    #3. Une methode GetRecord permettant de saisir et retourner le record mondial de l’épreuve concerné.
    #Remarque : le record doit avoir le même type de la nature du résultat
    def GetRecord(self):
        record = None
        nature = None
        while nature not in ['temps', 'distance', 'nombre de points']:
            nature = input("Entrez la nature du record (temps, distance, nombre de points) : ").lower()
        if nature == 'temps':
            record = int(input("Entrez le record mondial en secondes : "))
        elif nature == 'distance':
            record = float(input("Entrez le record mondial en mètres : "))
        elif nature == 'nombre de points':
            record = int(input("Entrez le record mondial en points : "))
        return record, nature
    #4. Une méthode SetResultat permettant d’ajouter le résultat à l’athlète concerné au dictionnaire DEprev.
    #Cette methode prend en paramètre l’objet athlète A dans cette épreuve.
    #Remarques :
    #▪ Le resultat peut être ajouté même si l’athlète n’est pas inscrit d’avance à l’épreuve
    #▪ Toutes les mise à jour nécessaires des attributs de cette classe doit être effectuées
    def SetResultat(self, athlète, resultat):
        if athlète in self._DEprev:
            self._DEprev[athlète] = resultat
        else:
            print(f"L'athlète {athlète.nom} {athlète.prenom} n'est pas inscrit à l'épreuve.")
    #5. Une méthode GetResultat permettant de retourner la valeur du résultat d’un athlète A
    #passé en paramètre. Un message d’inexistence doit être renvoyé si l’athlète ne participe pas à l’épreuve
    def GetResultat(self, athlète):
        if athlète in self._DEprev:
            return self._DEprev[athlète]
        else:
            return f"L'athlète {athlète.nom} {athlète.prenom} ne participe pas à cette épreuve."
    #6. Une méthode GestMédaillOr renvoyant le pays de l’athlète gagnant à l’épreuve et
    #ayant une médaille d’or.
    def GestMedailleOr(self):
        if not self._DEprev:
            return "Aucun athlète n'a participé à cette épreuve."
        gagnant = None
        meilleur_resultat = None
        for athlète, resultat in self._DEprev.items():
            if resultat is not None:
                if (meilleur_resultat is None or
                    (resultat.natR == 'temps' and resultat.valeur < meilleur_resultat.valeur) or
                    (resultat.natR == 'distance' and resultat.valeur > meilleur_resultat.valeur) or
                    (resultat.natR == 'nombre de points' and resultat.valeur > meilleur_resultat.valeur)):
                    meilleur_resultat = resultat
                    gagnant = athlète
        return gagnant.pays if gagnant else "Aucun gagnant déterminé."
