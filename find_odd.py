def find_it(seq):
    map = {}
    for num in seq:
        if num not in map:
            map[num] = 1
        else:
            map[num] += 1
    for key, value in map.items():
        if value % 2 != 0:
            return f"{key}"