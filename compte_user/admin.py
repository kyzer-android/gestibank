import logging
from sql.sql import connexion
from compte_user.user import User
from demande_crea.demande_crea_compte import DemandCreaCompte

class Admin(User):
    # cnx = connexion()

    def __init__(self, id):
        super().__init__("ADMIN",id)


    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.email,
                self.tel,
                self.debut_contrat)

        return str(test)

    def mise_a_jour(self, **kwargs):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "email": self.email,
                         "tel": self.tel})
        User.update("agent", self.id, **list_arg)

    def lister_demand_crea(self):
        cnx=connexion()
        cursor=cnx.cursor()
        cursor.execute("SELECT * FROM `demande_creacompte`")
        liste_obj=[]
        for element in cursor:
            liste_obj.append(DemandCreaCompte(element))
        cnx.close()
        return liste_obj


    def affecter_demande(self,agent):
        pass

    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.email,
                self.tel
                )

        return str(test)
if __name__ == "__main__":
    Objtest=Admin("0014")
    print(Objtest)
    liste_demande = Objtest.lister_demand_crea()
    i=0
    for liste in liste_demande:
        i+=1
        print(liste_demande[i])
