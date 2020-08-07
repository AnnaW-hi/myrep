import random
import string

def randomizer (length):

    password = ''

    for x in range(1, length):
        password += random.choice(characters)

    return password

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation

characters = []

characters.extend(lowercase)
characters.extend(uppercase)
characters.extend(punctuation)

print(lowercase)
print(uppercase)
print(string.punctuation)

count = 0

while True:

    password = ''
    try:
        length = int(input("Jak długie ma być hasło?"))
    except ValueError:
        print("Wpisz cyfrę")
    else:

        for x in range(1,length):
            password += random.choice(characters)

    for char in password:
        if char in punctuation:
            count += 1
            print("za dużo znaków specjalnych")
    if count > length/2:
        for char in password:
            if char in punctuation:
                password.replace(char, random.choice(characters))
                count -=1

    if password[0] not in uppercase:
        print("hasło musi zaczynać się wielką literą")




    print(password)
