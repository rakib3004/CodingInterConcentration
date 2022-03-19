def removeDuplicates(array):
    uniqueArray=[]

    uniqueArray.append(array[0])

    n=len(array)

    for i in range(1,len(array)):
        if array[i]!=array[i-1]:
            uniqueArray.append(array[i])


    return uniqueArray




array=[1, 2, 3, 4, 5, 6, 7, 3, 3, 4, 5, 6, 6, 6, 6, 7, 7, 7, 7]
array.sort()
array=removeDuplicates(array)
print(array)