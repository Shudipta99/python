class student:
    roll  =""
    gpa = "" 

    def __init__(self,roll,gpa) :#creating constructor in student class for auto call & giving value/parameter at obj creating time 
        self.roll = roll
        self.gpa = gpa

    def display (self): #function/method create for frequently object call
        print(f"Roll : {self.roll}, GPA: {self.gpa}")

rahim = student(101,3.75)
rahim.display()


karim = student(102,3.90)
karim.display()
