"""Le front renvoi un dictionnaire contenant toutes les valeurs"""
from errno import errorcode
from mysql.connector import connection
import logging


class DemandCreaCompte:
    def connexion(self, base_de_donne='Gestibank', user='root', password=''):
        try:
            cnx = connection.MySQLConnection(user=user, password=password,
                                             host='127.0.0.1', database=base_de_donne)
        except connection.errors.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.warning("Il y a un problème avec votre user name ou password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.warning("La base n’existe pas")
            else:
                logging.warning(err)
        else:
            logging.info(" connexion reussi")
            return cnx

    def __init__(self, valeur: dict):

        self.nom = valeur["nom"]
        self.prenom = valeur["prenom"]
        self.id = valeur["id"]
        self.mail = valeur["mail"]
        self.tel = valeur["tel"]
        self.adresse = valeur["adresse"]
        self.justificatif = valeur["justificatif"]
        self.valid = None
        self.affect = None

    def enregistrement(self, cnx=connexion()):  # Stocakge d'une demmande dans la base de donnee (table demande)

        cursor = cnx.cursor()

        try:
            insert_stmt = (
                "INSERT into demande_creation (nom,prenom,id,mail,telephone,adresse,justificatif)" "VALUES (%s ,%s, %s, %s,%s ,%s, %s)")
            data = [(self.nom, self.prenom, self.id, self.mail, self.tel, self.adresse, self.justificatif)]
            cursor.execute(insert_stmt, data)
            cnx.commit()

        except:
            logging.warning("Problème a l'insertion")
            return False

        else:
            return True

        cnx.close()

    def affectation(self, agent, cnx=connexion()):  # l'admin affect un client a un agent
        cursor = cnx.cursor()
        self.affect = agent
        try:
            affectation = ("UPDATE demande_creation SET id =" + self.id + "WHERE agent =" + self.agent)
            cursor.execute(affectation)
            cnx.commit()

        except:
            logging.warning("Problème d'affectation")
            return False
        else:
            return True
        cnx.close()

    def validation(self, valide, cnx=connexion()):  # L'agent valide le client
        cursor = cnx.cursor()
        self.affect = valide
        try:
            validation = ("UPDATE demande_creation SET id =" + self.id + "WHERE validation =" + self.valide)
            cursor.execute(validation)
            cnx.commit()

        except:
            logging.warning("Problème de validation")
            return False
        else:
            return True
        cnx.close()


""""
  def lister_demande(self): #Affiche toutes les demande en cours
        return list(dict)

    def selectionner_une_demande(self, dict, pos):  # recoit la list(dict) de lister_demande et renvoi un dict
        return dict[pos]

"""

if __name__ == "__main__":
    test = {"nom": "dieoz",
            "prenom": "marc",
            "id": "145",
            "mail": "truc@mac.com",
            "tel": "01546843",
            "adresse": "5 rue de la voie rouge 91216  Lamotte",
            "justificatif": "repertoir\distant\ "
            }

objet_test = DemandCreaCompte
