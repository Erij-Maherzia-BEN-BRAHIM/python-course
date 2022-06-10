class Point:
    def __init__(self,x,y) :
        self.x=x
        self.y=y
    def __str__(self):
        return f'{self.x} {self.y}'
        
        
class Robot:
    Version=0
    Nom=""
    def __init__(self,p=Point(0,0),o="Nord") :
        #assurer que o mawjouda f list
        assert o in  {'Nord', 'Est', 'Sud', 'Ouest'}
        self.__position=p
        self.__orientation=o
    def getPosition(self):
        return self.__position
    def getOrientation(self):
        return self.__orientation
    def setPosition(self,p):
        self.__position=p
    def setOrientation(self,o):
        #listO= {'Nord', 'Est', 'Sud', 'Ouest'}
        #if o in listO: 
        self.__orientation=o
        #else: print('pick one of these orientations: Nord, Est, Sud or Ouest')
    def TourneraDroite(self):
        if self.__orientation=="Nord":
            self.__orientation="Est"
        elif self.__orientation=="Est":
            self.__orientation="Sud"
        elif self.__orientation=="Sud":
            self.__orientation="Ouest"
        else: self.__orientation="Nord"
    def TournerGauche(self):
        if self.__orientation=="Nord":
            self.__orientation="Ouest"
        elif self.__orientation=="Ouest":
            self.__orientation="Sud"
        elif self.__orientation=="Sud":
            self.__orientation="Est"
        else: self.__orientation="Nord"

    def Avancer(self):
        if self.__orientation=="Nord":
            self.__position.y+=1
        elif self.__orientation=="Est":
            self.__position.x+=1
        elif self.__orientation=="Sud":
            self.__position.y-=1
        else: self.__position.x-=1
    def Reculer(self):
        if self.__orientation=="Nord":
            self.__position.y-=1
        elif self.__orientation=="Est":
            self.__position.x-=1
        elif self.__orientation=="Sud":
            self.__position.y+=1
        else: self.__position.x+=1
    def __str__(self):
        return f'{self.__position} {self.__orientation}'
R1=Robot()
x0=input('entrer le point de départ x: ')
y0=input('entrer le point de départ y: ')
R1.setPosition(p=Point(x0,y0))
o0=input("Entrer l'orientation de départ: ")
R1.setOrientation(o0)
x1=input("entrer le point d'arrivée x: ")
y1=input("entrer le point d'arrivée y: ")
o1=input("Entrer l'orientation d'arrivée: ")


def trajet(self, x,y,o):
    return
v=input('Entrer la version: ')
R1.Version=v
n=input('Entrer le nom: ')
R1.Nom=n
print(R1.Version , R1.Nom)

R1.Avancer()
R1.TourneraDroite()
R1.Avancer()

print(R1)

