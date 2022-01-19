import imp


import copy

oldList= [[1,2,3], [4,5,6], [7,8,9]]
newList= copy.copy(oldList)

print("Old list: ", oldList)
print("New list: ", newList)

#Adding elements to the old_list using shalllow copy
oldList.append([4,4,4])
newList.append([4,5,6])
print("Old list: ", oldList)
print("New list: ", newList)

#Adding new nested object using shallow copy
oldList[1][1]= 'ABC'
print("Old list: ", oldList)
print("New list: ", newList)

oldList[3][1]= 'DEF'
print("Old list: ", oldList)
print("New list: ", newList)

