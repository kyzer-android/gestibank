import logging
from sql.sql import connexion

logging.basicConfig(level=logging.DEBUG)


class User:
    def __init__(self, type_user, id):
        cnx = connexion()
        cursor = cnx.cursor()
        # Recuperation de la liste des nom de colone
        logging.debug("SELECT column_name FROM information_schema.columns WHERE table_name = '" + type_user +
                      "' AND table_schema='Gestibank';")
        cursor.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_name = '" + type_user + "' AND table_schema='Gestibank';")
        res = cursor.fetchall()
        # verifie si l'objet existe dans la BD grace a son id,si non le cree
        if not User.trouver_id(type_user, id):
            for colone in res:
                self.__setattr__(colone[0].lower(), None)
            self.id = id
        # cree un objet a partir des valeur de la BD
        else:
            for colone in res:
                command = ("Select " + colone[0] + " from " + type_user + " where id = " + id)
                logging.debug(command)
                cursor.execute(command)
                value = cursor.fetchone()
                self.__setattr__(colone[0].lower(), value[0])

    @classmethod  # mise a jour de la BD en fonction des paramètres de la type_user utiliser
    def update(self, type_user, id, **kwargs):
        cnx = connexion()
        cursor = cnx.cursor()
        if kwargs is not None:
            for key, value in kwargs.items():
                command = (" UPDATE `" + type_user + "` SET `" + key + "` = '" + value +
                           "' WHERE `client`.`ID` = '" + id + "';")
                logging.debug(command)
                cursor.execute(command)
                cnx.commit()
        cnx.close()

    @classmethod  # Si il n'existe pas dans la table du type_user cree une entree grace a l'id fournit
    def create(self, type_user, id):
        if not User.trouver_id(type_user, id):
            cnx = connexion()
            cursor = cnx.cursor()
            param = "Insert INTO " + type_user + "(ID) VALUES('" + id + "')"
            logging.debug(param)
            cursor.execute(param)
            cnx.commit()

    @classmethod  # Cherche une id dans une table
    def trouver_id(self, type_user, id):
        cnx = connexion()
        cursor = cnx.cursor()
        param = ("SELECT id from " + type_user + " WHERE ID ='" + id + "'")
        logging.debug(param)
        cursor.execute(param)
        test = cursor.fetchone()
        try:
            test[0] == id
        except:
            return False
        else:
            return True


if __name__ == "__main__":
    User.create("admin", "0sd01")
