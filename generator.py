from audioop import reverse


def my_generator():
    n = 1
    print("This is printed first")
    #generator function contains yield statments
    yield n
    n += 1

    print("This is printed second")
    yield n

    n=+1
    print("This is printed third")
    yield n

a = my_generator()
print("Using for loop..")
#Iterrating using for loop
for item in my_generator():
    print(item)

def reverse_string(my_string):
    length = len(my_string)
    for i in range(length -1,-1,-1):
        yield my_string[i]

        #for loop to reverse the strimg

for char in reverse_string("WORLD"):
    print (char)
