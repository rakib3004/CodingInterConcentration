def removeDuplicates(nums):
    n = len(nums)

    currentIndex =1

    for i in range(1,n):
        if nums[i]!=nums[i-1]:
            nums[currentIndex]=nums[i]
            currentIndex=currentIndex+1

    return nums,currentIndex


nums = [1,1,1,2,2,3,3,3,3,4,5,6,6,6,6,7,7,7,7]
new_nums,currentIndex=removeDuplicates(nums)
print(new_nums[:currentIndex])
print(nums[currentIndex:])
print(new_nums)
