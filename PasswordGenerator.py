'''
You're challenge for today is to create a random password generator!
For extra credit, allow the user to specify the amount of passwords to generate.
For even more extra credit, allow the user to specify the length of the strings he wants to generate!
'''

import random

try:
    numberOfPasswords = int(input('The ammount of passwords: '))
except ValueError:
    print('Thats not a proper value!')
    quit()

try:
    numberOfCharacters = int(input('The ammount of characters: '))
except ValueError:
    print('Thats not a proper value!')
    quit()

passwords = []
characterSet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '1','2','3','4','5','6','7','8','9','0',
                '!','"','£','#','$','%','^','&','*','(',')','_','+','.',',','?',':',';','`','~', ' ']

for i in range(0, numberOfPasswords):
    password = ''
    password = password.join(random.sample(characterSet, numberOfCharacters))
    passwords.append(password)
    
print('Passwords: {}'.format(passwords))
