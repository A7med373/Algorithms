from collections import defaultdict


def solution(s1, s2):
    l = 0
    for r in range(5,len(s2)):
        tmp = defaultdict(int)
        for letter in s1:
            tmp[letter] += 1
        if s2[r] not in tmp:
            l = r
        other = r
        while other < len(s2) and s2[other] in tmp:
            tmp[s2[other]] -= 1
            other += 1
        if max(tmp.values()) == 0 and min(tmp.values()) == 0:
            return True
    return False

s1="abc"
s2="cccccbabbbaaaa"
print(solution(s1, s2))