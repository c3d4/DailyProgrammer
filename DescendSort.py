import random

# Descending Sort
def descendingSort(list):
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

array = []
numberOfElements = int(input('Number of Elements: '))

for i in range(0, numberOfElements):
    array.append(random.randint(0, numberOfElements))

print(descendingSort(array))
