'''
create a short text adventure that will call the user by their name. 
The text adventure should use standard text adventure commands ("w, n, s, e, i, etc.").
for extra credit, make sure the program doesn't fault, quit, glitch, fail, or loop no matter what is put in, even empty text or spaces. 
'''

# Player Information 
position = [0,0]   
name = input('What is your name: ')     

def checkCommands():
    command = input()
    command = command.lower()
    if (command == 'left'):
        if (position[0] == 1 or position[0] == 0) and position[1] == 0:
            position[0] = position[0] - 1
            print('{0} moved left. Current position is {1}.'.format(name, position))
    elif (command == 'right'):
        if (position[0] == -1 or position[0] == 0) and position[1] == 0:
            position[0] = position[0] + 1
            print('{0} moved right. Current position is {1}.'.format(name, position))
    elif (command == 'up'):
        if (position[1] == -1 or position[1] == 0) and position[0] == 0:
            position[1] = position[1] + 1
            print('{0} moved upwards. Current position is {1}.'.format(name, position))
    elif (command == 'down'):
        if (position[1] == 1 or position[1] == 0) and position[0] == 0:
            position[1] = position[1] - 1
            print('{0} moved downwards. Current position is {1}.'.format(name, position))
    elif (command == 'help'):
        print('UP\r\nDOWN\r\nLEFT\r\nRIGHT\r\nINFO\r\nHELP\r\nQUIT')
    elif (command == 'info'):
        if (position[0] == 0 and position[1] == 0):
            print('{0} is at spawn.'.format(name))
        elif (position[0] == 0 and position[1] == 1):
            print('{0} is on the stairs.'.format(name))
        elif (position[0] == 0 and position[1] == -1):
            print('{0} is at the balcony.'.format(name))
        elif (position[0] == 1 and position[1] == 0):
            print('{0} is at the kitchen.'.format(name))
        elif (position[0] == -1 and position[1] == 0):
            print('{0} is at the armory.'.format(name))
    elif (command == 'quit'):
        quit()
    else:
        print('Invalid command. Type "HELP" for a list of commands')    

while True:
    checkCommands()
