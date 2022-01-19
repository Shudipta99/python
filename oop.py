class student:
    roll  =""
    gpa = ""

    def set_value(self,roll,gpa) :
        self.roll = roll
        self.gpa = gpa

    def display (self): #function/method create for frequently object call
        print(f"Roll : {self.roll}, GPA: {self.gpa}")
rahim = student()
rahim.set_value(101,3.75)
rahim.display()


karim = student()
karim.set_value(102,3.90)
karim.display()
