def removeDuplicates(array):

    uniqueArray = list(set(array))
    uniqueArray.sort()

    return uniqueArray

array= [1,2,5,6,2,42,3,5,3221,4,5,1,4,522,54,4,2,74,21,2,54,5,2,4,2,5,4,1,2]
print(removeDuplicates(array))