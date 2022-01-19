try:
    a = int(input("please enter the 1st number: "))
    b = int(input("please enter the2nd number: "))
    if(a<0):
       raise TypeError 
    c = a/b
    print(" {} / {} = {}".format(a,b,c))
except ZeroDivisionError:
    print("Divison by zero is not possible")
except ValueError:
    print("The data types are not correct")
except TypeError:
    print("The data is not in range")