'''
No more hiding from your alarm clock! You've decided you want your computer to keep you updated on the time so you're never late again.
A talking clock takes a 24-hour time and translates it into words.

Input Description:
An hour (0-23) followed by a colon followed by the minute (0-59).

Output Description:
The time in words, using 12-hour format followed by am or pm.

Sample Input data:
00:00
01:30
12:05
14:01
20:29
21:00

Sample Output data:
It's twelve am
It's one thirty am
It's twelve oh five pm
It's two oh one pm
It's eight twenty nine pm
It's nine pm
'''

import time, datetime, pyttsx3

while True:
    # Establish TTS Engine
    engine = pyttsx3.init()

    # Get the current time 
    date = datetime.datetime.now()
    date = str(date)
    
    # Trim the string 
    hour = date[11] + date[12]
    minutes = date[14] + date[15]

    # Get AM or PM
    amOrPm = 'AM'
    
    if int(hour) < 12:
        amOrPm = 'AM'
    else:
        amOrPm = 'PM'

    # Conversion from Military to Standard
    timeConvert = {
        '00': '12',
        '01': '1',
        '02': '2',
        '03': '3',
        '04': '4',
        '05': '5',
        '06': '6',
        '07': '7',
        '08': '8',
        '09': '9',
        '10': '10',
        '11': '11',
        '12': '12',
        '13': '1',
        '14': '2',
        '15': '3',
        '16': '4',
        '17': '5',
        '18': '6',
        '19': '7',
        '20': '8',
        '21': '9',
        '22': '10',
        '23': '11'
    }

    # Merge into a new time 
    newTime = '{}:{}'.format(timeConvert[hour], minutes)
    
    if (minutes == '00' or minutes == '30'):
        engine.say('It is {} {}.'.format(newTime, amOrPm))
        engine.runAndWait()
    time.sleep(5)
