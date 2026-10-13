import random 
import string

values = string.ascii_letters + string.punctuation + string.digits

n = int(input("Enter length of password: "))
password = ""

for i in range(n):
    password += random.choice(values)

print(f"Your random password is: {password}")