#agent
import logging
from sql.sql import connexion
from compte_user.userfuction import User


class Agent(User):
    # cnx = connexion()

    def __init__(self, id):
        super().__init__("AGENT", id)

    def flitre_compte(self):  # Filtre les demande de création de compte avec le matricule agent
        cnx = connexion()
        cursor = cnx.cursor()
        try:
            logging.debug("SELECT * FROM demande_creacompte WHERE affect = '" + self.matricule + "'")
            cursor.execute("SELECT * FROM demande_creacompte WHERE affect = '" + self.matricule + "'")
            True
        except:
            logging.warning("Erreur base de donnée")
            False

    def validation(self, agent_validation: bool):  # Validation création d'ouverture de compte
        cnx = connexion()
        cursor = cnx.cursor()
        self.valid = agent_validation
        # agent_validation = bool(input("Validez-vous cette création?"))
        if self.valid is True:
            cursor.execute("SELECT VALIDE FROM demande_creacompte affect 1")
        elif self.valid is False:
            cursor.execute("SELECT VALIDE FROM demande_creacompte affect 0")
        else:
            print("Erreur")

    def creation_compte_User(self, id):

        ajout_clien = ("INSERT INTO client (ID, NOM, PRENOM, MAIL, TEL, ADRESSE, JUSTIFICATIF)")
        demande_clien = ("VALUE FROM demande_creacompte (ID, NOM, PRENOM, MAIL, TEL, ADRESSE, JUSTIFICATIF)")

        try:
            if self.valid is True:  # @Si la demande est validé, création du compte, plus envoi un mail avec login/mdp
                cursor.execute(ajout_clien, demande_clien)
                """cursor.execute("INSERT INTO client (NOM, PRENOM, MAIL, TEL, ADRESSE, JUSTIFICATIF)"
                               "VALUE FROM demande_creacompte (NOM, PRENOM, MAIL, TEL, ADRESSE, JUSTIFICATIF)")"""

                # TODO Envoi d'un mail contenant l'id et le mot de passe


            elif self.valid is False:  # @sil la demande n'est pas valider (envoi de mail + demande mis en attente)
                pass
                # TODO Envoi d'un mail demandant les bonnes informations
            else:  # Erreur
                print("Erreur")
        except:
            logging.warning("Problème de validation")
        else:
            pass
            # TODO Création d'un compte banquaire par default avec la classe création de compte banquaire

    def modif_compte_User(self):  # Modification compte client
        pass

    def valid_cheque(self):  # Validation demande chéquier
        pass

    def valid_facilite(self):  # Validation facilité de caisse
        pass

    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.email,
                self.tel,
                self.debut_contrat)

        return (str(test))

    def mise_a_jour(self, **kwargs):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "email": self.email,
                         "tel": self.tel})
        User.update("agent", self.id, **list_arg)


if __name__ == "__main__":
    u = Agent("0000")
    logging.debug(u)

