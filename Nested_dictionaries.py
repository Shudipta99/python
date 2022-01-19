#Declaring and definig a nested dictionary
InfoOfStudent = {1: {'Name' : 'Swarna', 'Age': '25', 'Gender' : 'Female'},
                 2: {'Name' : 'Shama', 'Age': '24', 'Gender' : 'Female'},
                 3: {'Name' : 'Shreya', 'Age': '18', 'Gender' : 'Female'},
                 4: {'Name' : 'Mithila','Age': '23', 'Gender' : 'Female'},
                 }
 # Accessing elements of the dictionary

print(InfoOfStudent[4]['Age'])
del InfoOfStudent[4]['Age']
print(InfoOfStudent.items())

for s_id, s_info in InfoOfStudent.items():
    print("\nPerson Id:", s_id)

    for key in s_info:
        print(key + ':', s_info[key])