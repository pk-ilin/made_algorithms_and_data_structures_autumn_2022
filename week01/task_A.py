def insertion_sort(array: list[int]) -> None:
    size = len(array)

    for i in range(1, size):
        j = i
        while j > 0 and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1


n = int(input())
array = list(map(int, input().split()))

assert n == len(array)

insertion_sort(array)
print(" ".join(map(str, array)))
