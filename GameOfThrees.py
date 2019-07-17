'''
First, you mash in a random large number to start with. Then, repeatedly do the following:
If the number is divisible by 3, divide it by 3.
If it's not, either add 1 or subtract 1 (to make it divisible by 3), then divide it by 3.
The game stops when you reach "1".
'''

number = input('Number: ')

try:
    number = int(number)
except ValueError:
    print('Input not valid')

while number !=1:
    originalNumber = number
    number = number/3

    if number.is_integer() == False:
        number = originalNumber + 1
        print('Cant divide by {} by 3, turns into {}'.format(originalNumber, number))
        number = number / 3
        if number.is_integer() == False:
            number = originalNumber - 1 
            print('Cant divide by 3, turns into {}'.format( number))

            print(number)
            number = number /3 
    
    print(number)
    originalNumber = number
