"""
We can use an encoding approach where
we start with a number representing the length of the string,
followed by a separator character (let's use # for simplicity),
and then the string itself. To decode, we read the number until we reach a #,
then use that number to read the specified number of characters as the string.
"""
inp = ["we","say",":","yes","!@#$%^&*()"]
#inp = ["neet","code","love","you"]
def encode(strs):
    return ''.join(str(len(s)) + '#' + s for s in strs)

# 2#we3#say1#:3#yes10#!@#$%^&*()
def decode(s):
    if not s:
        return []
    result = []
    i = 0
    while i < len(s):
        j = s.find('#', i)
        length = int(s[i:j])
        i = j + 1
        result.append(s[i:i+length])
        i += length
    return result
print(decode(encode(inp)))