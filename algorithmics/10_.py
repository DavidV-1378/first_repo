# Given integer values, and a threshold, return the lenght of the longest consecutive run
# in which every value is at least the threshold. A lower value breaks the run, retun 0 for 
# empty input and no qualifying values. Do not modify the input. 

# [3, 7, 8, 9, 2, 9, 10, 11]
# treshold = 7
# return 3


def lenght_run(values: list[int], threshold: int) -> int:
    if not values:
        return 0
    count = 0
    longest_lenght = 0
    for value in values:
        if value >= threshold:
            count += 1
            longest_lenght = max(count, longest_lenght)
        else:
            count = 0
    return longest_lenght


# You are given a list of numbers, and several requests. Each reuqest specifies a sction of the list.
# Calcualte the sum of numbers in each requested section and return all the answers in order.
# Write a function "range_totals", each query is (start, end). Return one sum per query,
# in query order. Empty ranges are not allowed. Raise ValueError unless 0 <= start <= end <= len(values)

# [4, -2, 7, 1, 3, 5]
# (0, 3)

#[0], [0, 4], [0, 4, 2], [0, 4, 2, 9]

# (1, 4)
# values: 4, -2, 7, 1, 3

# prefix[4] - prefix[1] = 10 - 4 = 6

def range_totals(values: list[int], queries: list[tuple[int, int]]) -> list[int]:
    running_total = [0]
    totals = []
    for value in values:
        running_total.append(value + running_total[-1])
    for start, end in queries:
        if not 0 <= start <= end <= len(values):
            raise ValueError("Invalid range")
        totals.append(running_total[end] - running_total[start])
    return totals


# Return wether 2 entries at two diffrent positions sum to a target. Values may be negative or repeated.

def sum_positions(values: list[int], target: int) -> int:
    seen: set[int] = set()
    for value in values:
        if target - value in seen:
            return True
        seen.add(value)
    return False


