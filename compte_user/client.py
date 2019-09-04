#client
from compte_user.user import User
from sql.sql import connexion
import logging


class Client(User):
    def __init__(self, id):
        super().__init__("Client", id)

    def modifMDP(self, oldMDP, newMDP):
        cnx = connexion()
        cnx.autocommit = True
        cursor = cnx.cursor()
        try:

            data = ("SELECT PASSWORD FROM login WHERE id = " + self.id +
                    " and Password = PASSWORD('" + oldMDP + "')")
            logging.debug(data)
            cursor.execute(data)
            row = cursor.fetchone()
            changement = ("UPDATE login set Password = PASSWORD('" + newMDP +
                          "') where ID =" + self.id)

            logging.debug(changement)
            cursor.execute(changement)

            print("changement reussi")

        except Exception as e:
            logging.warning("Erreur de recherche ", e)
            logging.error(cursor.statement)

    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.mail,
                self.tel,
                self.adresse,
                self.justificatif)

        return(str(test))

    def mise_a_jour(self):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "mail": self.mail,
                         "tel": self.tel,
                         "adresse": self.adresse,

                         })
        User.update("client", self.id, **list_arg)


if __name__ == "__main__":
    x = Client('0021')
    print(x)
    x.mise_a_jour()

