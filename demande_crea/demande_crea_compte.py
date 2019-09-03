"""Le front renvoi un dictionnaire contenant toutes les valeurs"""
from errno import errorcode
from mysql.connector import connection
import logging

class DemandCreaCompte :
    def connexion(base_de_donne='Gestbank',user='root',password=''):
        try:
            cnx = connection.MySQLConnection(user=user, password=password,
                                             host='127.0.0.1', database=base_de_donne)
        except connection.errors.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logging.debug("Il y a un problème avec votre user name ou password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logging.debug("La base n’existe pas")
            else:
                logging.debug(err)
        else:
            logging.info(" connexion reussi")
            return cnx


    def __init__(self,valeur:dict,cnx=connexion()):

        self.nom=valeur["nom"]
        self.prenom=valeur["prenom"]
        self.id==valeur["id"]
        self.mail=valeur["mail"]
        self.tel=valeur["tel"]
        self.adresse=valeur["adresse"]
        self.justificatif=valeur["justificatif"]
        self.valid=None
        self.affect=None




    def enregistrement(self,cnx=connexion()): #Stocakge d'une demmande dans la base de donnee (table demande)

        cursor =cnx.cursor()


        try:
            insert_stmt = ("INSERT into demande_creation (nom,prenom,id,mail,telephone,adresse,justificatif)" "VALUES (%s ,%s, %s, %s,%s ,%s, %s)")
            data = [(self.nom,self.prenom,self.id,self.mail,self.tel,self.adresse,self.justificatif)]
            cursor.execute(insert_stmt, data)
            cnx.commit()
            cnx.close()

        except :
            return False

        else :
            return  True



    def affectation(self,agent): #l'admin affect un client a un agent
        return bool

    def validation(self, valide) :  #L'agent valide le client

        return bool


class User:
    def __init__(self,id,password,):



""""
  def lister_demande(self): #Affiche toutes les demande en cours
        return list(dict)

    def selectionner_une_demande(self, dict, pos):  # recoit la list(dict) de lister_demande et renvoi un dict
        return dict[pos]

"""

if __name__="__main__":
dico={"nom" :"dieoz",
      "prenom" :"marc",
      "id":"145",
      "mail": "truc@mac.com",
      "tel": "01546843",
      "adresse":"5 rue de la voie rouge 91216  Lamotte",
      "justificatif":"repertoir\distant\ "
}

