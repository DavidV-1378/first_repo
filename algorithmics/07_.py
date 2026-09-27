# Given non negative integers, return the lenght of the shortest non empty contiguous range, whose
# sum is at least the target.

values = [2, 1, 5, 2, 3, 2]
target = 7

left = 0
current = 0

# windows list: [2], [2, 1], [2, 1, 5], [1, 5], [1, 5, 2], [5, 2], [2]
# current = 2, 3, 8, 6, 8, 7, 2
# expend, expend, shrink, expend, shrink, shrink
# window lenght: 3, 3, 2

def shortest_range_at_least(values: list[int], target: int) -> int|None:
    if any(value < 0 for value in values):
        raise ValueError("Values must be non-negative.")
    
    left = 0 
    current = 0
    best: int|None = None
    
    for right, value in enumerate(values):
        current += value
        while current >= target and left <= right:
            window_lenght = right - left + 1
            if best > window_lenght or best is None:
                best = window_lenght
            current -= values[left]
            left += 1
    return best
    
# ticket_ids = ["t4", "t8", "t2"]

letters = ["a", "b", "c", "d", "a", "d", "b"]

def first_unique(letters: list[str]) -> str|None:
    count_lettrs:dict[str, int] = {}
    for letter in letters:
        count_lettrs[letter] = count_lettrs.get(letter, 0) + 1
    for letter in letters:
        if count_lettrs[letter] == 1:
            return letter
    return None
    
status = ["open", "closed", "open", "waiting"]

def index_by_value(status: list[str]) -> dict[str, list[int]]:
    positions: dict[str, list[int]] = {}
    for index, value in enumerate(status):
        if value not in positions:
            positions[value] = []
        positions[value].append(index)
    # positions.setdefault(value, []).append(index)
    return positions
    
text = "abba"

# Return the longest sub-string without repeated charcters.

"""
right         charcter        previous         left_after       current_window        best
  0              a              None               0                  "a"              1
  1              b              None               0                  "ab"             2
  2              b                1                2                  "b"              2
  3              a                0                2                  "ba"             2
"""

def lonegst_unique_sub_string(text: str) -> str:
    sub_strings: dict[str, int] = {}
    best = 0
    left = 0
    
    for right, charcter in enumerate(text):
        if charcter in sub_strings and sub_strings[charcter] >= left:
            left = sub_strings[charcter] + 1
        sub_strings[charcter] = right
        if right - left + 1 > best:
            best = right - left + 1
    return best
    

# Do any two diffrent positons in a list sum to the target?

def pair_exists(values: list[int], target: int) -> bool:
    for first in range(len(values)):
        for second in range(first + 1, len(values)):
            if values[first] + values[second] == target:
                return True
    return False
    
    
def pair_exists_hash(values: list[int], target: int) -> bool:
    