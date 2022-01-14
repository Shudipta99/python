from random import choice


def myAddition(x,y):
    print("performing the addtion op: ")
    return (x+y)
def mySubtraction(x,y):
    print ("performing the subtaction op: ")
    return(x-y)
def myMultiplication(x,y):
    print("performing the multiplication op: ")
    return(x*y)
def myDivision(x,y): 
    print("performing the division function op: ")
    return(x/y)

def myMenu():
    print("Main menu...")
    print("1> Addition op..")
    print("2> Subtraction op..")
    print("3> Multiplication op..")
    print("4> Division op...")
    ch = int(input("Please enter your option number: "))
    return ch
def calculation():
    ch = myMenu()
    num1 = int(input("please enter the first number: "))
    num2 = int(input("Please enter second number: "))
    if ch == 1:
        result = myAddition(num1,num2)
    elif ch == 2:
        result = mySubtraction(num1,num2)
    elif ch == 3:
        result = myMultiplication(num1,num2)
    elif ch == 4:
            result = myDivision (num1,num2)
    print ("So result = ", result)
calculation()
        