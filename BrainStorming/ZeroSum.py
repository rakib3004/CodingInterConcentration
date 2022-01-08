def two_sum(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i]+ numbers[j] == 0:
                return numbers[i], numbers[j]



numbers = [2,1,4,7,5,-7,4,65,3,8]

number1, number2 = two_sum(numbers)

print(number1,number2)