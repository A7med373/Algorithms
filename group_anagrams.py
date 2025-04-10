"""
Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
"""
from typing import List
Input = ["act","pots","tops","cat","stop","hat"]

def solution(strs: List[str]) -> List[List[str]]:
    map = {}
    big_guy = [[0] * 26 for _ in range(len(strs))]
    for i in range(len(strs)):
        for j in range(len(strs[i])):
            big_guy[i][ord(strs[i][j]) - ord('a')] += 1
        key = tuple(big_guy[i])
        if key not in map:
            map[key] = []
        map[key].append(strs[i])
    return list(map.values())

print(solution(Input))