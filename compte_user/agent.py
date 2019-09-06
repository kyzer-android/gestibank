# agent
import logging
from sql.sql import connexion
from compte_user.user import User
from demande_crea.demande_crea_compte import DemandCreaCompte as Creation
import datetime
from compte_bancaire.compte import Compte


class Agent(User):
    # cnx = connexion()

    def __init__(self, id):
        super().__init__("AGENT", id)

    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.mail,
                self.tel,
                self.debut_contrat)
        return str(test)



    @classmethod
    def cree_compte_agent(self, valeur):
        cnx = connexion()
        cursor = cnx.cursor()
        if type(valeur) == type(dict()):
            logging.debug("inside dict")
            id = valeur["id"]
            nom = valeur["nom"]
            prenom = valeur["prenom"]
            mail = valeur["mail"]
            tel = valeur["tel"]
            debut_contrat = datetime.date.today()
            logging.debug(debut_contrat)

            ajout_clien = ("INSERT INTO agent (ID, NOM, PRENOM, MAIL, TEL, DEBUT_CONTRAT)"
                           "VALUES ( %s, %s, %s, %s, %s, %s)")
            demande_clien = (id, nom, prenom, mail, tel, debut_contrat)

        try:
            cursor.execute(ajout_clien, demande_clien)
            cnx.commit()
        except Exception as e:
            logging.warning("problème d'insertion ", e)
        finally:
            cnx.close()

    def mise_a_jour(self, **kwargs):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "mail": self.mail,
                         "tel": self.tel})
        User.update("agent", self.id, **list_arg)

    def flitre_compte(self):  # Retourne les demande de création de compte avec le id agent
        cnx = connexion()
        cursor = cnx.cursor()
        requette = "SELECT * FROM demande_creacompte WHERE affect = '" + self.id + "'"
        try:
            logging.debug(requette)
            cursor.execute(requette)
            liste_crea = cursor.fetchall()

            for demande in liste_crea:
                logging.debug(demande)
        except:
            logging.warning("Erreur base de donnée")
        else:
            liste_obj = []
            for element in liste_crea:
                liste_obj.append(Creation(element))
            return liste_obj

    def validation_Crea(self, objet_demandecrea, valid_crea: bool):  # Validation création d'ouverture de compte
        objet_demandecrea.validation(valid_crea)
        logging.debug(objet_demandecrea)
        if objet_demandecrea.valid is True:  # Si la demande est validé, création du compte, envoi un mail avec login/mdp + mis en True
            # TODO envoi de mail avec id/mdp
            objet_demandecrea.creation_compte_client()
            self.creation_Compte_Bank(objet_demandecrea.id) #Création compte banquaire

        elif objet_demandecrea.valid is False:  # Si la demande n'est pas valider = envoi de mail demande info + mis en False
            pass  # TODO envoi de mail avec une demande d'info supplementaire
        else:  # Erreur
            print("Erreur/En attente")

    def creation_Compte_Bank(self, id):
        Compte.creation_compteban(id)


    """
    def modif_compte_client(self, client):  # Modification compte client
        pass

    def valid_cheque(self):  # Validation demande chéquier
        pass

    def valid_facilite(self):  # Validation facilité de caisse
        pass
"""

if __name__ == "__main__":
    # u = Agent("0000")
    # list = u.flitre_compte()
    # print(type(list[1]))
    # test = {"nom": "dieoz",
    #         "prenom": "marc",
    #         "id": "14sdsd5",
    #         "mail": "truc@mac.com",
    #         "tel": "01546843"
    #         }


    test = Agent("999")
    test2 = {"nom": "dieoz",
            "prenom": "marc",
            "id": "145",
            "mail": "truc@mac.com",
            "tel": "01546843",
            "adresse": "5 rue de la voie rouge 91216  Lamotte",
            "justificatif": "repertoir\distant\ ",
            "affect" :  "999"
            }
    test3 = Creation(test2)
    test.validation_Crea(test3, False)



