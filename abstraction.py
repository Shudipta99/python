from abc import ABC,abstractmethod  #create abstract class


class Shape(ABC):
    def __init__(self, dim1,dim2):
        self.dim1= dim1
        self.dim2= dim2

    @abstractmethod   #create abstract method for a model an it uses universal
    def area(self):     # abstract method has no body
        pass                #abstract class has no no object

class Triangle(Shape):  #Here triangle class inherit abstract class
                        #abstract class has no no object
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of Triangle : ",area)
 
class Rectangle(Shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ",area)

t1= Triangle(20,30)
t1.area()

r1= Rectangle(15,25)
r1.area()