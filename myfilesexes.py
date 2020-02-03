from myfile import sortMethod

def indexer(listValue,myValue):
    """ Takes in an unsorted list, sorts it
     and returns index of sorted value- myValue and sorted list newSort"""

    newSort = sortMethod(listValue)
    indexPos = newSort.index(myValue)
    return indexPos, newSort

case1 = [1,4,5,6,3,5,3,77,9,3,89,6,99,0,56,565,454,4,5,7,3,4,343,2,3,3,43,23,4]
index_77,newSortedList = indexer(case1,77)
print([index_77,newSortedList])

