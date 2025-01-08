class C_Matiere:
    def __init__(self, id_matiere, coef, intutile):
        self.id_matiere = id_matiere
        self.coef = coef
        self.intutile = intutile

    def Set_matiere(self):
        self.id_matiere = input("Donner l'id de la matière: ")
        self.coef = int(input("Donner le coefficient de la matière: "))
        self.intutile = input("Donner l'intitulé de la matière: ")

    def get_matiere(self):
        return (self.id_matiere, self.coef, self.intutile)


class C_Module:
    def __init__(self, id_M, nb_credit):
        self.id_M = id_M
        self.nb_credit = nb_credit
        self.Matieres = []  

    def Get_Module(self):
        module_dict = {self.id_M: self.Matieres}
        return module_dict

    def Set_Module(self, id_matiere, coef, intitulé):
        if len(self.Matieres) < 2:
            matiere = C_Matiere(id_matiere, coef, intitulé)
            self.Matieres.append((matiere.id_matiere, matiere.coef, matiere.intutile))
        else:
            print("Un module ne peut contenir que deux matières.")


class C_Etudiant:
    def __init__(self, id_Et, nom, prenom, spécialité):
        self.id_Et = id_Et
        self.nom = nom
        self.prenom = prenom
        self.spécialité = spécialité
        self.notes = []

    def Set_Etudiant(self, id_Et, nom, prenom, spécialité, notes):
        self.id_Et = id_Et
        self.nom = nom
        self.prenom = prenom
        self.spécialité = spécialité
        self.notes = notes

    def Get_Etudiant(self):
        return [[self.id_Et, self.nom, self.prenom, self.spécialité, self.notes]]

    def Get_Notes_Etudiant(self):
        return self.notes

    def Set_Notes(self, id_matiere, note):
        self.notes.append((id_matiere, note))
    
    def Affiche_Notes(self):
        if self.notes:
            print("Notes pa étudiant")
            print(f"ID etudiant: {self.id_Et}):")
            for id_matiere, note in self.notes:
                print(f"ID Matière: {id_matiere}, Note: {note}")
