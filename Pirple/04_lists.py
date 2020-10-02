myUniqueList = []
myLeftovers = []

def Leftovers(n):
    myLeftovers.append(n)
    return myLeftovers

def UniqueFunction(n):
    if n not in myUniqueList:
        myUniqueList.append(n)
        return myUniqueList
    else: Leftovers(n)


while len(myUniqueList) < 10:
    n = input('Insert whatever you want: ' )
    UniqueFunction(n)
    
print('myUniqueList is: ', myUniqueList)
print()
print('myLeftovers are: ', myLeftovers)

