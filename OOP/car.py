 from mimetypes import init


class Car:

    #initialisation lezem t7ot fiha self
    def __init__(self,nName, nModel, nColor, nCompany ):
        self.name=nName
        self.model=nModel
        self.color=nColor
        self.company=nCompany

    def left(self):
        print ('move to the left')
    def right(self):
        print ('move to the right')

c1=Car('X','5','blue','BMW')
print(c1.color)

print('x'*130)
c2=Car('X','1','red','BMW')
#print(c2.color)
