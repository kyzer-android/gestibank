import logging
from sql.sql import connexion
import random

class Compte:
    def __init__(self,id_compte):

        cnx = connexion()
        cursor = cnx.cursor()
        param = ("SELECT `ID_compte`, `Type_compte`, `Date_creation`, `Rib`"
                 " FROM `compte` WHERE ID_compte = "+ str (id_compte))
        cursor.execute(param)
        element = cursor.fetchone()
        logging.debug(element)
        self.ID_compte= element[0]
        self.Type_compte = element[1]
        self.Date_creation = element[2]
        self.Rib = element[3]

def Creation_compteban():
    pass


def __str__(self):
    test = (self.ID_compte,
            self.Type_compte,
            self.Date_creation,
            self.Rib,
            self.Valeur_depas,
            self.Solde,
            self.CC_Decouverte,
            self.AGIOS)

    return str(test)
x= Compte(1002)
print(x)


