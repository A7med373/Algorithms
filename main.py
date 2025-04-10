""""
Дан некоторый алфавит и строка. Необходимо найти
в строке панграмму минимальной длины, где панграмма -
это такая подстрока исходной строки,
в которую входят все буквы из алфавита (но необязательно только они).

Пример:
A = {a, b, c}
s = "dfagabkaceb"
Ответом могут быть строки "bkac" и "aceb"
"""
A = {'a', 'b', 'c'}
s = "dfagabkaceb"
def solution(A, s):
    need = {char: 1 for char in A}
    have = {}
    required = len(need)
    formed = 0
    l = 0
    minl = float('inf')
    min_window = ""
    for r in range(len(s)):
        char = s[r]
        if char in need:
            have[char] = have.get(char, 0) + 1
            if have[char] == need[char]:
                formed += 1
        while formed == required:
            if r - l + 1 < minl:
                minl = r - l + 1
                min_window = s[l:r+1]
            left_char = s[l]
            if left_char in need:
                have[left_char] -= 1
                if have[left_char] < need[left_char]:
                    formed -= 1
            l += 1

    return min_window if min_window else None

print(solution(A, s))