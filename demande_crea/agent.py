import mysql.connector as mysql
import logging
from sql import connexion
from demande_crea_compte import DemandCreaCompte as Creation


class Agent:
    cnx = mysql.connect(host="localhost", user="root", password="", database="gestibank")

    def __init__(self, **arg):
        self.id ==
        self.nom =
        self.prenom =
        self.type_user =
        self.matricule =
        self.email =
        self.tel =
        self.debut_contrat =
        self.valid = None


    def flitre_compte(self):
        cnx = connexion()
        cursor = cnx.cursor()







    def validation(self): #Validation création d'ouverture de compte
        cnx = connexion()
        cursor = cnx.cursor()

        try:
            if:
                cursor.execute(

                )
            elif:
                cursor.execute(

                )
        except:
            logging.warning("Problème de validation")
            return False


    def config_compte(self): #Configuration compte client




    def modif_compte(self): #Modification compte client




    def valid_cheque(self): #Validation demande chéquier





    def valid_facilite(self): #Validation facilité de caisse
