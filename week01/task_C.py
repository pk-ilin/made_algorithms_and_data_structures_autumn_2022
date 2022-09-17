def merge(inv1: int, array1: list[int], inv2: int, array2: list[int]) -> list[int]:
    n1 = len(array1)
    n2 = len(array2)

    i, j = 0, 0
    array = []
    inv = inv1 + inv2

    while i + j < n1 + n2:
        if i == n1 or (j < n2 and array2[j] < array1[i]):
            array.append(array2[j])
            j += 1
        else:
            array.append(array1[i])
            if j > 0 and array1[i] > array2[j - 1]:
                inv += j
            i += 1

    return inv, array


def merge_sort(array: list[int]) -> list[int]:
    size = len(array)
    if size < 2:
        return 0, array

    middle = size // 2

    left_inv, left_array = merge_sort(array[: middle])
    right_inv, right_array = merge_sort(array[middle:])

    return merge(left_inv, left_array, right_inv, right_array)


def get_inv_count(array: list[int]) -> int:
    inv, _ = merge_sort(array)
    return inv


n = int(input())
array = list(map(int, input().split()))

assert n == len(array)

inv = get_inv_count(array)
print(inv)
