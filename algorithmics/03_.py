from dataclasses import dataclass

#One-pass scans

def count_positive(numbers: list(int)) -> int:
    count = 0
    for number in numbers:
        if number >= 0:
            count += 1
    return count
    
# [4, -1, 2]
# count: 0, 1, 1, 2
# O(n) time complexity

# [6, 2, 9, 4]
# running state = information we carry from 
#one step to the next.

def largest(numbers: list(int)) -> int:
    if not numbers:
        raise ValueError("List cannot be empty")
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max
    
# value | best_before | value > best? | best_after | prefix |
#   6   |      6      |       0       |     6      |    [6] |  
#   2   |      6      |       0       |     6      |  [6, 2]|
#   9   |      6      |       1       |     9      | [6, 2, 9]|
#   4   |      9      |       0       |     9      | [6, 2, 9, 4]|

# loop invariant = a statement that is True after every iteration
# O(1) auxiliary / memory space

def total(numbers: list(int)) -> int:
    total = 0
    for number in numbers:
        total += number
    return total
    
# [4, 2, 3]
# total: 0, 4, 6, 9
# O(n) time complexity
# auxiliary space = O(1)

def count_target(values: list(str), target: str) -> int:
    count = 0
    for value in values:
        if value == target:
            count += 1
    return count
    
# values[open, closed, open, waiting], target: open
# invariant: after proccesing i values, count equals number of 
#targets found among the values.

# Return the index of the first value that is smaller than the value immediately before it.
# List: [3, 5, 7, 4, 8]

def first_drop(values: list[int] -> int|None:
    for index in range(1, len(values)):
        if values[index] < values[index - 1]:
            return index
    return None

# index: 0, 5 < 3, 
# index: 1, 7 < 5, 
# index: 2, 4 < 7,
# index: 3, 8 < 4
# index: 4, 5 < 8 

# List of sensor readings. In one-pass, return max, min, total and number of readings.
# [6.0, 2.5, 9.0, 4.5]

@dataclass(frozen = True)
class Summary:
    max: float
    min: float
    total: float
    count: int
    
def summarise(values: list[float]) -> Summary:
    if not values:
        raise ValueError("List of values cannot be empty")
    max = values[0]
    min = values[0]
    total = 0.0
    count = 0
    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value
        total += value
        count += 1
    return Summary(max, min, total, count)
    
    
    
# [5, 2, 9, 9 ,7]
# Second largest distinct value.
# 5: 5, None
# 2: 5, 2
# 9: 9, 5
# 9, 9, 5
# 7, 9, 7

def second_distinct_largest(values: list[int]) -> int|None:
    first: int|None = None
    second: int|None = None
    for value in values:
        if value == first or value == second:
            continue
        if first is None or value > first:
            second = first
            first = value
        elif second is None or value > second:
            second = value
    return second