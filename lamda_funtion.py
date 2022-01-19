myList=[1,3,4,5,6,8,11,12]
newList=list(filter(lambda x: (x%2 == 0), myList))
print(newList)

myList= [1,5,4,6,8,11,3,12]
newList= list(map(lambda x: x * 2, myList))
print(newList)