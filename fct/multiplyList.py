from unittest import result


def multiplyList(l):
    resultat=1
    for i in l:
        resultat*=i
    return resultat
lista=[1,2,3,4,5]
print(multiplyList(lista))

