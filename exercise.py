class triangle:#create class named triangle
    def __init__(self,base,height):#create constructor
        self.base= base
        self.height= height

    def calculate_area(self):#create method/function
        area = 0.5 * self.base * self.height
        print ("Area = ", area)

t1 = triangle(10,20)
t1.calculate_area()

t2 = triangle(30,40)
t2.calculate_area()

