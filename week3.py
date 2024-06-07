import random

length = input("How long do you want your password to be? ")

# Weak Password: only lowercase letters
password = ''
lowercase = 'abcdefghijklmnopqrstuvwxyz'
for i in range(int(length)):
    randChar = random.choice(lowercase)
    password = password + randChar
print("Weak Password: " + password)

# Moderate Password: lowercase and uppercase letters
password2 = ''
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(length)):
    randChar = random.choice(lowercase + uppercase)
    password2 = password2 + randChar
print("Moderate Password: " + password2)

# Strong Password: lowercase, uppercase, numbers, and special characters
password3 = ''
specialChars = '1234567890~!@#$%^&*()-_=+[{]}'
for i in range(int(length)):
    randChar = random.choice(lowercase + uppercase + specialChars)
    password3 = password3 + randChar
print("Strong Password: " + password3)
