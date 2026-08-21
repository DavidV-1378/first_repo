def range_total(
    values: list[int],
    start: int,
    end: int
    ) -> int:
    total = 0
    for index in range(start, end):
        total += values[index]
    return total
    
# values = [5, 2, 7, 3]
# start = 1
# end = 4

#[1, 2, 3, 4]
#index = 1 total = 2
#index = 2 total = 7

# sales = [5, 2, 7, 3, 6]
# prefix = 0
# boundry 0  1  2  3   4   5
# values   5  2  7   3   6
# prefix 0  5  7  14  17  23

# sales[start:end] = 1, 2, 3
# [0, len(values)]

# sales[1:4] = 12
# prefix[4] = 5 + 2 + 7 + 3 = 17
# prefix[1] = 5
# prefix [4] - prefix[1] = sales[1:4]

def prefix_sums(values: list[int]) -> list[int]:
    prefix = [0]
    running_sum = 0
    for value in values:
        running_sum += value
        prefix.append(running_sum)
    return prefix
    
    # worst case time, for q queries: O(qn)
    
def range_sum(prefix: list[int], start: int, end: int) -> int:
    if not 0 <= start <= end < len(prefix):
        raise IndexError("Invalid range")
    return prefix[end] - prefix[start]
    
    # worst case time, for q queries: O(q)
    # build time: O(n)
    # total time: O(q+n)
    # extra / auxillary space: O(n)
    
# Readings: [4.0, 8.0, 10.0, 3.0, 12.0]. Threshold: 8.0. 
#   Alert : [0  ,  1 ,   1 ,  0 ,   1 ]. 
#  Prefix : [0  ,  0 ,   1 ,  2 ,   2,   3].

def alert_prefix(values: list[float], threshold: float) -> list[int]:
    prefix = [0]
    for value in values:
        is_alert = value >= threshold
        prefix.append(prefix[-1] + int(is_alert))
    return prefix