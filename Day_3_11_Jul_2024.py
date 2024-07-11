# -----------------AKSHAY PROBLEM DEFINITION---------------

# ip = input("Enter the no : ")
# cal = int(ip)+int(ip*2)+int(ip*3)
# print(cal)

# ------------------------------------------------------------
'''Write a Python program to get a newly-generated string from a given string 
where "Is" has been added to the front. Return the string unchanged if the given 
string already begins with "Is". '''

# def generate_string(ip):

#     if ip.startswith("Is"):
#         return ip
#     else :
#         return "Is"+ip 

# ip = input("Enter the string : ")
# print(generate_string(ip))

# ----------------------------PROJECT_1----------------------------------------

class Student:
    def __init__(self, name, roll_no, sub_1, sub_2):
        self.name = name
        self.roll_no = roll_no
        self.sub_1 = sub_1
        self.sub_2 = sub_2

    def accept_input(self, name, roll_no, sub_1, sub_2):
        obj = Student(name, roll_no, sub_1, sub_2)
        my_list.append(obj)

    def display(self):
        for student in my_list:
            print(f"Name: {student.name}")
            print(f"Roll No: {student.roll_no}")
            print(f"Subject 1: {student.sub_1}")
            print(f"Subject 2: {student.sub_2}")
            print("------------")

    def search(self, rn):
        for i in range(len(my_list)):
            if my_list[i].roll_no == rn:
                return i
        return -1

    def delete(self, rn):
        i = self.search(rn)
        if i != -1:
            del my_list[i]
            print(f"Record with roll no {rn} deleted.")
        else:
            print(f"Record with roll no {rn} not found.")

    def update(self, on, nn):
        i = self.search(on)
        if i != -1:
            my_list[i].roll_no = nn
            print(f"Record updated: old roll no {on} to new roll no {nn}.")
        else:
            print(f"Record with roll no {on} not found.")

my_list = []

obj = Student('', 0, '', '')

while True:
    print("\nSelect Operation")
    print("1. Accept Student Details")
    print("2. Display Student Details")
    print("3. Search Student Details")
    print("4. Delete the Record")
    print("5. Update the Record")
    print("6. Exit")

    ch = int(input("Enter the choice: "))
    if ch == 1:
        nm = input("Enter Name: ")
        roll_no = int(input("Enter the roll no: "))
        sub_1 = input("Enter the first subject: ")
        sub_2 = input("Enter the second subject: ")
        obj.accept_input(nm, roll_no, sub_1, sub_2)
    elif ch == 2:
        obj.display()
    elif ch == 3:
        ip = int(input("Enter the roll no to search: "))
        index = obj.search(ip)
        if index != -1:
            print("Record found:")
            student = my_list[index]
            print(f"Name: {student.name}")
            print(f"Roll No: {student.roll_no}")
            print(f"Subject 1: {student.sub_1}")
            print(f"Subject 2: {student.sub_2}")
        else:
            print("Record not found.")
    elif ch == 4:
        ip = int(input("Enter the roll no to delete: "))
        obj.delete(ip)
    elif ch == 5:
        ip1 = int(input("Enter the roll no to update: "))
        ip2 = int(input("Enter the new roll no: "))
        obj.update(ip1, ip2)
    elif ch == 6:
        print("Thank you")
        break
    else:
        print("Invalid choice. Please try again.")

