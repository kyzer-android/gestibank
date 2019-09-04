import mysql.connector as mysql
import logging
from sql import connexion
from demande_crea.user import User



class Agent(User):


    def __init__(self, id):
        super().__init__("AGENT", id)


    """def flitre_compte(self):
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
    """

    def afficher(self):


        test = (self.id,
        self.nom,
        self.prenom,
        self.type_user,
        self.email,
        self.tel,
        self.debut_contrat)

        print(str(test))

u = Agent( "00014")
u.afficher()