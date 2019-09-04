import mysql.connector as mysql
import logging
from sql import connexion
logging.basicConfig(level=logging.DEBUG)

def affiche_donne_curs(curs):
    for ligne in curs:
        print(ligne)


def identification(ID):
        Statut=False
        cnx=connexion()
        cursor=cnx.cursor()
        cursor.execute("SELECT * FROM `login` WHERE ID = "+ID)
        row=cursor.fetchone()
        if cursor.rowcount==-1
            logging.info("")

identification("0020")


