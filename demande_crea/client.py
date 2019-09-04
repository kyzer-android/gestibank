from demande_crea import user
from sql import connexion
import  logging


class client (user) :
    def __init__(self,id):
        cnx = connexion()
        cursor = cnx.cursor()
        try :
            result  = ("Select mail ,tel,adresse,justificatif from client  where id = "+id)
            cursor.execute(result)
            row = cursor.fetchone()
            if cursor.rowcount == -1 :
                logging.warning("Utilisateur Inconnu")
            elif cursor.rowcount == 1 :
                print(row)
            else :
                logging.warning("Erreur de parametre")
            self.mail = row[0]
            self.tel = row[1]
            self.adresse = row[2]
            self.justificatif = row[3]
            
        except :
            logging.warning("Probleme de recherche ")

x=client("0020")
print(x)

   # def acces (self):
      #  user.identification()


