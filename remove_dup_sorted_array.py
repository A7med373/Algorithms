def remove_duplicates_from_sorted_array(array: list[int]) -> int:
    if not array:
        return 0

    i = 0
    for j in range(len(array)):
        if array[j] != array[i]:
            i += 1
            array[i] = array[j]
    print(list(array))
    return i + 1