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




# remplir la table compteBAnc aléatoirement
"""def peuplement_compteBanc(ligne_bd, cnx):
            cursor = cnx.cursor()
            stmt=("INSERT INTO `compte` (`ID_compte`, `Type_compte`, `Date_creation`, `Rib`, `Valeur_depas`, `Solde`, `CC_Decouverte`, `AGIOS`) "
                  "VALUES (%s, %s, %s, %s, %s,%s, %s, %s);")
            insert_stmt = (
                "INSERT INTO demande_creacompte (`ID_compte`, `Type_compte`, `Date_creation`, `Rib`, `Valeur_depas`, `Solde`, `CC_Decouverte`, `AGIOS`)"
                "VALUES (%s, %s, %s, %s, %s,%s, %s, %s)"
            )
            logging.debug(stmt)
            cursor.execute(stmt,ligne_bd)
            logging.debug(cursor)
            cnx.commit()
            cnx.close()

for i in range(11, 25):
    ID_compte = '100' + str(i)
    Type_compte = 'nom' + str(i)
    Date_creation = 'prenom_' + str(i)
    Rib = str(random.randint(1000000000, 9999999999))
    Solde = str(random.randint(1000000000, 9999999999))
    ligne = (ID_compte, Type_compte, Date_creation, Rib, 'Valeur', Solde, 'True', 'Valeur')
    peuplement_compteBanc(ligne, connexion())"""


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


