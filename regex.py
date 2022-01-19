import re

animalStr= "Cat rat mat fat pat"

allAnimals= re.findall("[crmpf]at", animalStr)
for i in allAnimals:
    print(i)
print()

numStr= "123 12345 123456 1234567"

print("Matches: ", len(re.findall("\d{5,7}", numStr)))
