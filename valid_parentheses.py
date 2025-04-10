def solution(s):
    stack = []
    if not s:
        return False
    valid = {ord('[') + ord(']'), ord('{') + ord('}'), ord('(') + ord(')')}
    for c in s:
        if stack and ord(c) + ord(stack[-1]) in valid and ord(c) > ord(stack[-1]):
            stack.pop()
        else:
            stack.append(c)
    return True if not stack else False

string = "{(){}{}}"
print(solution(string))


