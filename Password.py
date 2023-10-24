import random
import secrets
import string

#Promting the user to write the length of password needed
length = int(input("Enter password length: "))

#Ensuring the password length is 8 characters
if length<8:
    length = 8
#Defining the characters for the password
characters = string.ascii_letters + string.digits + string.punctuation

password = []
for i in range(length):
    randomchar = random.choice(characters)
    password.append(randomchar)

print("Random Password: " + "".join(password))
