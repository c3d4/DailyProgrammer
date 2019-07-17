def sumRange():
    numberRange = [int(input('Enter Min Value: ')), int(input('Enter Max Value: '))]
    sumVar = numberRange[0]
    for i in range(numberRange[0], numberRange[1]+1):
        sumVar = sumVar+i
    return sumVar

print(sumRange())
