import string
import random

#simple random password generator

def generatePassword(length):
    #adds all letter, digits, and symbols
    char = string.ascii_letters + string.digits + string.punctuation

    #picks random letters, digits, and punctuations
    password = ''.join(random.choice(char) for _ in range(length))

    return password

#records user password length, then prints out random password
length = int(input("Password length: "))
print(f"Password: {generatePassword(length)}\n")