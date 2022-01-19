age = int(input("please enter the age of the person: "))
if age < 5:
    print("To young")
elif ((age > 5) and (age <= 17)):
    grade = age -5
    print("Go to {}  grade".format(grade))
else:
    print("Go to college")