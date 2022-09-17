def merge(array1: list[int], array2: list[int]) -> list[int]:
    n1 = len(array1)
    n2 = len(array2)

    i, j = 0, 0
    array = []

    while i + j < n1 + n2:
        if j == n2 or (i < n1 and array1[i] < array2[j]):
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1

    return array


def merge_sort(array: list[int]) -> list[int]:
    size = len(array)
    if size < 2:
        return array

    middle = size // 2

    left_array = merge_sort(array[: middle])
    right_array = merge_sort(array[middle:])

    return merge(left_array, right_array)


n = int(input())
array = list(map(int, input().split()))

assert n == len(array)

array = merge_sort(array)
print(" ".join(map(str, array)))
