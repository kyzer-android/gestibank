import logging
from sql.sql import connexion
from compte_user.user import User

class Admin(User):
    # cnx = connexion()

    def __init__(self, id):
        super().__init__("ADMIN", id)


    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.email,
                self.tel,
                self.debut_contrat)

        return str(test)

    def mise_a_jour(self, **kwargs):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "email": self.email,
                         "tel": self.tel})
        User.update("agent", self.id, **list_arg)