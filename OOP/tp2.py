class Etudiant:
    __D={}
    __id=0
    def __init__(self,n,p):   
        self.nom=n
        self.prenom=p
        self.__note1=0
        self.__note2=0
        self.__note3=0
    def SaisieNote(self):
        self.__note1=input(float('veuillez saisir la note 1'))
        self.__note2=input(float('veuillez saisir la note 2'))
        self.__note3=input(float('veuillez saisir la note 3'))
    def Enregistrer(self):
        return