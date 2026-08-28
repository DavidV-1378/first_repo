values = [4, 6, 3]

# [0, 4, 10, 13]

#  index: 0 1 2  3  4 
# values: 2 5 8 11 14
#         L         R
# values[0],  values[len(values - 1)]

values = [1, 3, 4, 6, 8, 10]
target = 12

# Given an soreted list and a target, return the indexes of two different values, whose sum equals
#the target.

#   L = 0,  R = 5
# values[L] = 1, values[R] = 10
# 1 + 10 = 11 < 12, L += 1

# L = 1, R = 5
# 3 + 10 = 13 > 10, R -= 1

def sum_equals_target(values: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(values) - 1
    while right > left:
        current = values[left] + values[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return None
    
print(sum_equals_target(values, target))

#r a c e c a r

def is_palindrom(text: str) -> bool:
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True
    
values = [10, 20, 30, 40, 50]

def reverse_in_place(values: list[int]) -> None:
    left = 0
    right = len(values) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
        
reverse_in_place(values)
print(values)

x = (10,)

values = [4, -2, 7, -1, 0]

def keep_non_negative(values: list[int]) -> int:
    write = 0
    for read in range(len(values)):
        if values[read] >= 0:
            values[write] = values[read]
            write += 1
    return write

lenght = keep_non_negative(values)
print(values[:lenght])

# read value keep?      write       write_after  result
#  0     4    yes   values[0] = 4        1        [4]
#  1     -2   no         -               1        [4]
#  2     7    yes   values[1] = 7        2        [4, 7]
#  3     -1   no         -               2        [4, 7]
#  4     0    yes   values[2] = 0        3        [4, 7, 0]