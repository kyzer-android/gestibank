#agent
import logging
from sql.sql import connexion
from compte_user.user import User
from demande_crea.demande_crea_compte import DemandCreaCompte as Creation


class Agent(User):
    # cnx = connexion()

    def __init__(self, id):
        super().__init__("AGENT", id)

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



    def flitre_compte(self):  # Retourne les demande de création de compte avec le id agent
        cnx = connexion()
        cursor = cnx.cursor()
        requette = "SELECT * FROM demande_creacompte WHERE affect = '" + self.id + "'"
        try:
            logging.debug(requette)
            cursor.execute(requette)
            liste_crea = cursor.fetchall()

            for demande in liste_crea :
                logging.debug(demande)
        except:
            logging.warning("Erreur base de donnée")
        else:
            liste_obj = []
            for element in liste_crea:
                liste_obj.append(Creation(element))
            return liste_obj

    def validation_Crea(self, objet_demandecrea, valid_crea:bool): # Validation création d'ouverture de compte
        objet_demandecrea.validation(valid_crea)
        if objet_demandecrea.valide is True: # Si la demande est validé, création du compte, envoi un mail avec login/mdp + mis en True
            # TODO envoi de mail avec id/mdp
            # TODO création de compte banquaire
            objet_demandecrea.creation_compte_User()
        elif objet_demandecrea.valide is False: # Si la demande n'est pas valider = envoi de mail demande info + mis en False
            pass # TODO envoi de mail avec une demande d'info supplementaire
        else:  # Erreur
            print("Erreur/En attente")


"""

    def modif_compte_User(self):  # Modification compte client
        pass

    def valid_cheque(self):  # Validation demande chéquier
        pass

    def valid_facilite(self):  # Validation facilité de caisse
        pass
"""



#TEST
if __name__ == "__main__":
    u = Agent("0000")
    list = u.flitre_compte()
    print(type(list[1]))
