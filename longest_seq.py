"""
Hint:
We can consider a number num as the start of a sequence
if and only if num - 1 does not exist in the given array.
We iterate through the array and only start building the sequence
if it is the start of a sequence. This avoids repeated work.
We can use a hash set for O(1) lookups by converting the array to a hash set.


"""

array = [5,20,4,10,3,4,2] # 4
#array = [0,3,2,5,4,6,1,1]  # 7

def solution(nums):
    nums = set(nums)
    length = 1
    for num in nums:
        temp = 1
        if num - 1 in nums:
            continue
        while num + 1 in nums:
            temp += 1
            num += 1
        length = max(length, temp)
    return length

print(solution(array))