# Sorting, ordering, and stability

# Insertion sort

values = [5, 2, 4, 6, 1]

# [5], [2, 5], [2, 4, 5], [2, 4, 5, 6], [1, 2, 4, 5, 6]

# values = [2, 5, 7, 4]

# [2, 5, 7, 7], [2, 5, 5, 7]

# Already sorted input = O(N), Worse case input = O(N^2)

def insertion_sort(values: list[int]) -> None:
    for i in range(1, len(values)):
        current = values[i]
        j = i - 1
        while j >= 0 and current < values[j]:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = current

# Selection sort

# (N - 1) + (N - 2) + (1) = N * (N - 1) / 2 = (N ^ 2 - N) / 2 = O(N ^ 2)

values = [4, 2, 5, 1, 3]

def selection_sort(values: list[int]) -> None:
    for left in range(len(values) - 1):
        smallest = left
        for i in range(left + 1, len(values) - 1):
            if values[i] < values[smallest]:
                smallest = i
            if smallest != left:
                values[left], values[smallest] = (values[smallest], values[left],)

# Bubble sort

# [4, 2, 3, 1], [2, 4, 3, 1], [2, 3, 4, 1], [2, 3, 1, 4],
# [2, 3, 1, 4]
# [2, 1, 3, 4]
# [1, 2, 3, 4]

# Worst case input = O(N ^ 2)

# Best case input = O(N)

values = [4, 2, 3, 1]

def bubble_sort(values: list[int]) -> None:
    for end in range(len(values) - 1, 0, -1):
        swap = False
        for i in range(end):
            if values[i] > values[i + 1]:
                values[i], values[i + 1] = (values[i + 1], values[i])
                swap = True
        if not swap:
            break