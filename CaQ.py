min, max = 0, 100 
n = max /2 

while (input('Is {0} your number? '.format(int((max + min) / 2))) == 'F'):
    if (input('Is your number higher or lower than {0}: '.format(int((max + min) / 2))) == 'L'):
        max = int((max + min) / 2)
    else:
        min = int((max + min) / 2)     
