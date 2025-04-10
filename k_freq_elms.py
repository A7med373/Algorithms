"""
Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

"""
from typing import List

nums = [1,2,2,2,2,3,3,3]
k = 2
def solution(nums, k):
    count = {}
print(solution(nums, k))

# def solution(nums: List[int], k: int) -> List[int]:
#     hashm = {}
#     for num in nums:
#         if num not in hashm:
#             hashm[num] = 1
#         else:
#             hashm[num] += 1
#     hashm = dict(sorted(hashm.items(), key=lambda item: item[1], reverse=True))
#     return list(hashm.keys())[:k]
