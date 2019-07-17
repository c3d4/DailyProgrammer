# Remove a specific character from a list/array
def removeChar(char, list):
    for i in list:
        if i == char:
            list.remove(i)
    return list

# Decending Sort
def decendingSort(list):
    tempList = []

    def findMaximum(nList):
        maximum = 0 
        for i in list: 
            if i > maximum:
                maximum = i
        return maximum
    
    while (len(list) != 0):
        tempList.append(findMaximum(list))
        list.remove(findMaximum(list))
        findMaximum(list)

    list = tempList
    return list 

# Length check of list
def lengthCheck(check, list):
    if (check > len(list)):
        return True
    else:
        return False

# N-1 to N in SEQUENCE for X in RANGE(0, N)
def frontElim(iteration, list):
    for i in range(0, iteration):
        list[i] -= 1
    return list

# Havel-Hakimi Algorithm
def hh(list):
    while True: 
        removeChar(0, list)
        if (len(list) == 0):
            return True
        list = decendingSort(list)
        N = list[0]
        list.remove(N)
        if (lengthCheck(N, list) == True):
            return False 
        frontElim(N, list)

print(hh([12, 12, 12, 12, 12, 12, 12, 12, 12]))
