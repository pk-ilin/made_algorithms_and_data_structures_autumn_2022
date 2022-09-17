def roman_to_int(value: str) -> int:
    res = 0
    size = len(value)
    SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50}

    i = 0
    while i + 1 < size:
        if SYMBOLS[value[i + 1]] > SYMBOLS[value[i]]:
            res += SYMBOLS[value[i + 1]] - SYMBOLS[value[i]]
            i += 2
        else:
            res += SYMBOLS[value[i]]
            i += 1

    if i < size:
        res += SYMBOLS[value[i]]

    return res


def greater(value1: (str, str, int), value2: (str, str, int)) -> bool:
    if value1[1] > value2[1]:
        return True
    elif value1[1] == value2[1]:
        return value1[2] > value2[2]

    return False


def insertion_sort_modified(array: list[(str, str, int)]) -> None:
    size = len(array)

    for i in range(1, size):
        j = i
        while j > 0 and greater(array[j - 1], array[j]):
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1


n = int(input())
kings = []

for _ in range(n):
    full_name = input()
    name, num = full_name.split()
    num = roman_to_int(num)
    kings.append((full_name, name, num))

assert n == len(kings)

insertion_sort_modified(kings)
print("\n".join([king[0] for king in kings]))
