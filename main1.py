"""
Задача с собеседования в Яндекс

Дан некоторый алфавит и строка. Необходимо найти в строке панграмму минимальной длины,
где панграмма - это такая подстрока исходной строки,
в которую входят все буквы из алфавита (но необязательно только они).

Пример:
Ответом могут быть строки "bkac" и "aceb"
"""
A = {'a', 'b', 'c'}
s = "dfagabkaceb"

def is_complete(myset, string):
    for letter in myset:
        if letter not in string:
            return False
    return True
def at_least_one(myset, string):
    for letter in string:
        if letter in myset:
            return True
    return False
def duplicates(myset, string):
    if len(string) <= 1:
        return False
    unique = set()
    for letter in string:
        if letter in unique:
            if letter in myset:
                return True
            else:
                continue
        else:
            unique.add(letter)
    return False

def solution(A, s):
    i = 0
    result = ''
    while not is_complete(A, result) and i < len(s) - 1:
        result = result + s[i]
        if duplicates(A, result):
            result = ''
        if not at_least_one(A, result):
            result = ''
        i += 1
    return result

print(solution(A, s))