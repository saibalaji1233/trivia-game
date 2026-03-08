import random
import string
def generate_password():
# ask user for password preferences
    length=int(input("Enter password length:"))
    upper=input("Do you want uppercase letters?(yes/no):").lower()
    special=input("Do you want special characters?(yes/no):").lower()
    digits=input("Do you want digits?(yes/no):").lower()
# basic characters (small letters)
    characters=string.ascii_lowercase
# add other characters if user wants
    if upper=="yes":
        characters+=string.ascii_uppercase
    if special=="yes":
        characters+=string.punctuation
    if digits=="yes":
        characters+=string.digits
# generate password
    password=""
    for i in range(length):
        password+=random.choice(characters)
    return password
# call the function
result=generate_password()
print("Generated Password:",result)
