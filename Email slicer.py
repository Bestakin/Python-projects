import re


email = input("Enter email address: ")
#Defining a pattern expression to match the eamil address

pattern = r'^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})$'
#using pattern to search for matches in the email
match = re.match(pattern, email)

if match:
    username = match.group(1)
    domain = match.group(2)
    print("Username:", username)
    print("Domain:", domain)
else:
    print("no email address.")



