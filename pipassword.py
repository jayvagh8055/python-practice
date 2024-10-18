import random

# Letters (a to z)
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

# Numbers (0 to 10 as strings)
numbers = [str(i) for i in range(101)]  # Convert numbers to strings

# Common Symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', 
           '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']

# Password variable
password = []
print("Welcome to the password maker!")
nt_latter = int(input("How many letters do you want? "))
nt_number = int(input("How many numbers do you want? "))
nt_symbole = int(input("How many symbols do you want? "))

# Generate password
for _ in range(nt_latter):
    password.append(random.choice(letters))

for _ in range(nt_number):
    password.append(random.choice(numbers))

for _ in range(nt_symbole):
    password.append(random.choice(symbols))

# Output the generated password
print("Generated Password:", password)
passe=""
for char in password:
    passe += char
print(f"your password is :{passe}")



#out put
#Welcome to the password maker!
#How many letters do you want? 2
#How many numbers do you want? 2
#How many symbols do you want? 2
#Generated Password: ['x', 't', '99', '72', ',', '[']
#your password is :xt9972,[
