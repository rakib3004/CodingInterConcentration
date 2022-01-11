def binary_search(array, leftElement, rightElement, targetElement):
    if leftElement > rightElement:
        return -1
    while leftElement<= rightElement:
        middleObject = (leftElement + rightElement) // 2

        if array[middleObject] == targetElement:
            return middleObject
        if array[middleObject] < targetElement:
            leftElement = middleObject+1
        else:
            rightElement = middleObject-1
    return  -1

def efficient_two_sum(numbers):
    numbers.sort()
    n = len(numbers)
    for i in range(n-1):
        target = 0 - numbers[i]
        target_index = binary_search(numbers, i+1, n-1, target)
        if target_index > i:
            return  target_index