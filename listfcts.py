def pairList(l):
    resultat=[]
    for x in l:
        if x%2==0:
            resultat.append(x)
    return resultat
def impairList(l):
    resultat=[]
    for x in l:
        if x%2==1:
            resultat.append(x)
    return resultat


numbs=[1,2,3,4,5,7,5,6,8,45,66,88,66,89,100]
print(pairList(numbs))
print(impairList(numbs))