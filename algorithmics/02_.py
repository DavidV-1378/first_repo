def first_zero(values: list[int]) -> int | None:
    for index, value in enumerate(values):
        if value == 0:
            return index
    return None

first_zero([5, 0, 3])

# index = 0, value = 5
# index = 1, value 0 -> return 1

def contains_with_count(
        values: list[str],
        target: str
) -> tuple[bool, int]:

    checks = 0
    for value in values:
        checks += 1
        if value == target:
            return True, checks
    return False, checks
    
contains_with_count(["a", "b", "c"], "c")

# a == c, checks = 1
# b == c, checks = 2
# c == c, checks = 3 -> return True, 3

# ["a", "b", "c", "d"], n = 4
# ["a"] n = 1

# linear growth - O(n)

def first_item(values: list[int]) -> int:
    return values[0]
    
# constant growth - O(1)

def print_all(values: list[int]) -> None:
    for value in values:
        print(value) 
        
# linear growth O(n)

def print_all_order_pairs(values: list[int]) -> None:
    for left in values:
        for right in values:
            print (left, right)
            
print_all_order_pairs([1, 2])

# left = 1, right = 1 
# left = 1, right = 2
# left = 2, right = 1
# left = 2, right = 2

# output - (1, 1), (1, 2), (2, 1), (2, 2)

# n = 1, output = 1 
# n = 2, output = 4 
# n = 3, output = 9

# quadatric growth - O(n^2)

# O(1) - constant amount of work
# O(n) - procces each item 
# O(n^2) - procces pairs of items

# if n chages from 10 to 100: 
# 0(1) will stay the same.
# 0(n) 10 times the work.
# 0(n^2) 100^2 -> 10000; 100 times the work.

def count_even(values: list[int]) -> int:
    count = 0
    for value in values:
        if value % 2 == 0:
            count += 1
    return count
            
# [1, 4, 7]
# 1, False
# 4, True
# 7, False
# return 1
# 0(n) - linear

def has_duplicated_slow(values: list[int]) -> bool:
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if values[left] == values[right]:
                return True
    return False
    
print(range(len([4, 7, 9])))

# [4, 7, 9]
# left = 0, right = 1, 4 == 7, False
# left = 0, right = 2, 4 == 9, False
# left = 1, right = 2, 7 == 9, False
# return False
# O(n^2

usernames = ["anna", "dan", "alex", "david"]
queries = ["anna", "ioan", "alex"]

def answer_with_list(
    usernames: list[str],
    queries: list[str]
    ) -> list[bool]:
    
    results: list[bool] = []
    for query in queries:
        results.append(query in usernames)
    return results 
    
print(answer_with_list(usernames, queries) ==[True, False, True])

# O(n*q) - linear

def answer_with_set(
    usernames: list[str],
    queries: list[str]) -> list[bool]:
    
    usernames_set = set(usernames) # O(n)
    results = []
    for query in queries: # q repetitions
        results.append(query in usernames_set) # O(1)
    return results
    
# set membership is O(1)

# O(n + q) - linear