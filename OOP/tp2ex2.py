import random
class Personne:
    def __init__(self):
        self.nom=input('entrer le nom: ')
        self.prenom=input('entrer le prenom: ')
        self.age=int(input('entrer l"age: '))
class Deeeee:
    def __init__(self):
        self.__numface=0
    def lancerDe(self):
        self.__numface=random.randint(1,6)
    def getvaleurDe(self):
        return self.__numface
class Joueur(Personne):
    def __init__(self):
        Personne.__init__(self)
        self.d1=Deeeee()
        self.d2=Deeeee()
        self.score=0
    def Jouer(self):
        self.d1.lancerDe()
        l1= self.d1.getvaleurDe()
        self.d2.lancerDe()
        l2= self.d2.getvaleurDe()
        s=l1+l2
        return s

        
        
    def __str__(self):
        return f'{self.nom} {self.prenom} {self.age} {self.score}' 

p1=Joueur()
p2=Joueur ()
while(p1.score<100 and p2.score<100):
    x=p1.Jouer()
    y=p2.Jouer()
    if x>y:
        p1.score+=10
        print(p1,p1.score)
    elif x<y:
        p2.score+=10 
        print(p2,p2.score)

    else:
        continue
if p1.score>p2.score:
            print("The first player is the winner")
if p1.score<p2.score:
            print("The second player is the winner")

