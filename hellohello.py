
def student_info():
    name = input("Enter student name: ")
    email = input("Enter email address: ")
    number = input("Enter number: ")
    gender = input("Enter gender: ")
    age = input("Enter age: ")

    Student_files = {'name' : name,'gender' : gender,'age' : age,'number' : "numbers",}
    # Print student information
    return Student_files
    # print("Name:", name)
    # print("Email:", email)
    # print("Number:", number)
    # print("Gender:", gender)
    # print("Age:", age)

# Call the function to collect and display student information
student_info()
