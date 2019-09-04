from demande_crea.user import User

from sql import connexion
import  logging


class client (User) :
    def __init__(self,id):
        super().__init__("Client", id)


    def modifMDP (self,oldMDP,newMDP):
        cnx=connexion()
        cnx.autocommit=True
        cursor=cnx.cursor()
        try:

            data = ("SELECT PASSWORD FROM login WHERE id = "+self.id +
                    " and Password = PASSWORD('"+oldMDP+"')")
            logging.debug(data)
            cursor.execute(data)
            row = cursor.fetchone()
            changement= ("UPDATE login set Password = PASSWORD('" + newMDP +
                             "') where ID =" + self.id)

            logging.debug(changement)
            cursor.execute(changement)


            print("changement reussi")

        except Exception as e:
            logging.warning("Erreur de recherche ",e)
            logging.error(cursor.statement)




    def afficher(self):
            test = (self.id,
                    self.nom,
                    self.prenom,
                    self.type_user,
                    self.mail,
                    self.tel,
                    self.adresse,
                    self.justificatif)

            print(str(test))

x=client('0021')
x.afficher()

x.modifMDP('oussama','oussa')
#print (x)
   # def acces (self):
      #  user.identification()


