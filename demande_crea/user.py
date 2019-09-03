import mysql.connector as mysql
import logging

logging.basicConfig(level=logging.DEBUG)


class User:
    def identification(login, password):
        pass

    def __init__(self, id, password, ):
        pass


def connexion(base_de_donne='Gestibank', user='root', password=''):
    try:
        cnx = mysql.connection.MySQLConnection(user=user, password=password,
                                               host='127.0.0.1', database=base_de_donne)
    except mysql.connection.errors.Error as err:
        if err.errno == mysql.errorcode.ER_ACCESS_DENIED_ERROR:
            logging.debug("Il y a un problème avec votre user name ou password")
        elif err.errno == mysql.errorcode.ER_BAD_DB_ERROR:
            logging.debug("La base n’existe pas")
        else:
            logging.debug(err)
    else:
        logging.info(" connexion reussi")
        return cnx





def definit_user_type(login,cnx=connexion()):
    cursor = cnx.cursor()
    try:

        cursor.execute("SELECT * FROM client where id = " + login)
        cnx.commit()
    except mysql.Error as e:
        if e.errno == -1:
            try:
                cursor.execute("SELECT * FROM agent where id = " + login)
                cnx.commit()
            except mysql.Error as f:
                if f.errno == -1:
                    try:
                        cursor.execute("SELECT * FROM admin where id = " + login)
                        cnx.commit()
                    except mysql.Error as g:
                        if g.errno == -1:
                            logging.warning("L'utilisateur n'existe pas")

                        else:
                            logging.info("L'utilisateur est du type admin")

                else:
                    logging.info("L'utilisateur est du type agent")
        else:
            logging.info("L'utilisateur est du type client")


definit_user_type("0020")
