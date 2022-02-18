import random
import string

print("Welcome To Your Password Generator")
print("==================================")

letters = string.ascii_letters
digits = string.digits
punc = string.punctuation

chars = letters + digits + punc

number = input("Amount of passwords to generate: ")
number = int(number)

length = input("Your password length: ")
length = int(length)

print('\nhere are your passwords:')
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)