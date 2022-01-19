# Operator overloading
class myPoint :
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

#Overloading + operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y  = other.y
        return myPoint(x,y)

p1 = myPoint(1,2)
p2 = myPoint(3,4)
print(p1)
print(p2)

print(p1<p2)