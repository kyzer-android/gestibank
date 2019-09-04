import mysql.connector as mysql
import logging
from sql import connexion
logging.basicConfig(level=logging.DEBUG)
class User:
    def __init__(self,type_user,id):
        cnx = connexion()
        cursor = cnx.cursor()
        logging.debug("SELECT column_name FROM information_schema.columns WHERE table_name = '" + type_user +
                      "' AND table_schema='Gestibank';")
        cursor.execute(
            "SELECT column_name FROM information_schema.columns WHERE table_name = '" + type_user + "' AND table_schema='Gestibank';")
        res=cursor.fetchall()

        for colone in res:
            command=("Select " + colone[0] + " from " + type_user + " where id = " + id)
            logging.debug(command)
            cursor.execute(command)
            value=cursor.fetchone()
            self.__setattr__(colone[0].lower(),value[0] )


    def affiche_donne_curs(curs):

        for ligne in curs:
            print(ligne)


    def identification(ID):
            Statut=False
            cnx=connexion()
            cursor=cnx.cursor()
            cursor.execute("SELECT * FROM `login` WHERE ID = "+ID)
            row=cursor.fetchone()
            if cursor.rowcount==-1:
                print("Utilisateur innconnu")
            elif cursor.rowcount==1:
                 print(row)
            else :
                print("erreur de paramètre")

def affiche_client(client):
    print("nom:{},Prenom :{},")
    type_user="client"
    id="0020"
if __name__=="__main__":
    u=User("client","0020")




