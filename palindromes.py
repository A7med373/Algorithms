string = "Was it a car or a cat I saw?"

def solution(s):
    l, r = 0, len(s) - 1
    while l < r:
        while not s[l].isalnum() and l < r:
            l += 1
        while not s[r].isalnum() and r > l:
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
        return True
print(solution(string))