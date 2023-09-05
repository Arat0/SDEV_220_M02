"""
Arat Palacios-Suarez 
M02 lab - case study: if else and while 
this app store student info and Gpa. its also tells you which students made it into the Dean's list and Honor roll 
"""

students = []

continue_add = True


while continue_add:
    last_name = input("Enter the student's last name :")
    first_name = input("Enter the students's first name: ")
    gpa = float(input("Enter student's GPA: "))
    
    students_dict = {'last_name':last_name , 'first_name' : first_name , 'gpa' : gpa} 
    students.append(students_dict)
    
    
    x = input("Enter 1 to input another student or 2 to continue: ")
    if x == '2':
        continue_add = False  # Set the Boolean variable to False to exit the loop
    elif x != '1':
        print("Invalid input. Please enter either 1 or 2.")

for student in students:
    if student['gpa'] >= 3.5:
        print(f"{student['first_name']} {student['last_name']} is on the Dean's List.")
    elif student['gpa'] >= 3.25:
        print(f"{student['first_name']} {student['last_name']} is on the Honor Roll.")
