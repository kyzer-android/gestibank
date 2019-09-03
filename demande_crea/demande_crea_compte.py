"""Le front renvoi un dictionnaire contenant toutes les valeurs"""


class DemandCreaCompte:
    def __init__(self,valeur:dict):
        self.nom
        self.prenom
        self.id
        self.Mail
        self.tel
        self.adresse
        self.justificatif
        self.valid
        self.affect
        pass

    def enregistrement(self): #Stocakge d'une demmande dans la base de donnee (table demande)
        return bool


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