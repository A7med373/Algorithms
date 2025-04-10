from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    l, r = 0, 0
    # length = r - l + 1
    count = defaultdict(int)
    result = 0
    while r < len(s) - 1:
        count[s[r]] += 1
        while r - l + 1 - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1
        result = max(result, r - l + 1)
        r += 1

    return result

s="AAABABB"
k=1