# -----------------AKSHAY PROBLEM DEFINITION---------------

# ip = input("Enter the no : ")
# cal = int(ip)+int(ip*2)+int(ip*3)
# print(cal)

# ------------------------------------------------------------
'''Write a Python program to get a newly-generated string from a given string 
where "Is" has been added to the front. Return the string unchanged if the given 
string already begins with "Is". '''

def generate_string(ip):

    if ip.startswith("Is"):
        return ip
    else :
        return "Is"+ip 

ip = input("Enter the string : ")
print(generate_string(ip))