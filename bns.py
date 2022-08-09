
def BinarySearch(array, findValue):
    mid = len(array)
    middleV = array[mid//2]
    while True:
        if findValue == middleV:
            return findValue
        elif findValue > middleV:
            mid = len(array)/2
            middleV = array[mid//2]
        else:
            pass
            
    
array = [1, 2, 3, 4, 5]
BinarySearch(array, 3)