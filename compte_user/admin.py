import logging
from sql.sql import connexion
from compte_user.user import User
from demande_crea.demande_crea_compte import DemandCreaCompte
from datetime import date


class Admin(User):
    # cnx = connexion()

    def __init__(self, id):
        super().__init__("ADMIN", id)

    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.mail,
                self.tel,
                self.debut_contrat)

        return str(test)

    def mise_a_jour(self, **kwargs):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "mail": self.mail,
                         "tel": self.tel})
        User.update("agent", self.id, **list_arg)

    def lister_demand_crea(self):
        cnx = connexion()
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM `demande_creacompte`")
        liste_obj = []
        for element in cursor:
            liste_obj.append(DemandCreaCompte(element))
        cnx.close()
        return liste_obj

    def affecter_demande(self, objet, agent):
        objet.affectation(agent)

    @classmethod
    def cree_compte_agent(self, valeur):
        if User.trouver_id('agent', valeur["id"]) is False:
            cnx = connexion()
            cursor = cnx.cursor()
            if type(valeur) is type(dict()):
                # logging.debug("inside dict")
                id = valeur["id"]
                nom = valeur["nom"]
                prenom = valeur["prenom"]
                mail = valeur["mail"]
                tel = valeur["tel"]
                debut_contrat = str(date.today())

                ajout_client = ("INSERT INTO `agent` (`ID`, `NOM`, `PRENOM`, `TYPE_USER`, `MAIL`,"
                                " `TEL`, `DEBUT_CONTRAT`) VALUES  ( %s, %s, %s, %s, %s, %s, %s)")
                demande_client = (id, nom, prenom ,'AGENT', mail, tel, debut_contrat)
                logging.debug(ajout_client + str(demande_client))

            try:
                cnx = connexion()
                cursor = cnx.cursor()
                cursor.execute(ajout_client, demande_client)
                cnx.commit()
                logging.info("insertion réussi")
            except Exception as e:
                logging.warning("Erreur insertion", e)
            finally:
                cnx.close()
        else:
            logging.warning("L'Agent  Existe déjà ")


    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.mail,
                self.tel
                )

        return str(test)


if __name__ == "__main__":
    # Objtest=Admin("0014")
    # print(Objtest)
    # liste_demande = Objtest.lister_demand_crea()
    # i=0
    # for liste in liste_demande:
    #     i+=1
    #     print(liste_demande[i])
    test = {"id": "14fd55r5",
            "nom": "dieoz",
            "prenom": "marc",
            "mail": "truc@mac.com",
            "tel": "01546843"
            }
    print("{}".format(test))
    Admin.cree_compte_agent(test)
