"""old"""

# 1.
# input - a list of numbers.
# output - a integer that shows how many numbers below 0
# are present in the inputted list.
# edge case - a empty list.

# 2.
# prediction: 8
# 1. 0 + 6 = 6
# 2. 6 + -2 = 4
# 3. 4 + 4 = 8
# result: 8

# 3.
# ["cat", "dog", "cheeta", "wolf"] -> "cheeta"
# ["apple", "pear", "kiwi", "grape"] -> None
# ["carrot", "potato", "pea", "bean"] -> "carrot"
#
# 1. Parse each string in the list.
# 2. Check if the lenght of the str is greater than 5.
# 3. If greater than 5, return the string immediately (so it is the first word).
# 4. If end is reached and no string is greater than 5, return None.
#
def first_long_word (words: list[str]) -> str | None:
    for word in words:
        if len(word) > 5:
            return word
    return None


"""new"""


""" 
1)
input = list of integers
output = count of how many negative numbers 
edge case = empty list ( [] )

2)
6   total: 0
-2  total: 1
4   total: 1

3)
Example:
["cat", "pigeon", "dog"]
["apple", "pear", "grape"]
["pineaple", "watermelon", "grapefruit"]

1. Parse the list of values.
2. Check lenght of values
3. If larger than five, return the value
4. If no value was found, return None

"""
def longer_than_five(values: list[str]) -> str | None:
    for value in values:
        if len(value) > 5:
            return value
    return None

print(longer_than_five(["cat", "pigeon", "dog"]))

"""4)"""

def any_negative(values: list[int]) -> bool:
    for value in values:
        if value < 0:
            return True
    return False

"""5

Normal example:
("10:00", "INFO", "Start"), ("10:01", "ERROR", "Timeout"), ("10:02", "INFO", "End") -> ((1, ("10:01", "ERROR", "Timeout")), 2)

Empty example:
[] -> (None, 0)

First-error example:
("10:00", "ERROR", "Crash immediately"), ("10:01", "INFO", "Running") -> ((0, ("10:00", "ERROR", "Crash immediately")), 1)

Later-error example:
("10:00", "INFO", "A"), ("10:01", "WARN", "B"), ("10:02", "INFO", "C"), ("10:03", "ERROR", "D") -> ((3, ("10:03", "ERROR", "D")), 4)

No-error example:
("10:00", "INFO", "Boot"), ("10:01", "WARN", "High memory") -> (None, 2)

Trace:
   index             entry                  entry[1]       error?    checked         do next
    0	   ("09:00", "INFO", "Ok")	         "INFO"	       False	    1	    Move to next iteration
    1	   ("09:01", "WARN", "Low battery")	 "WARN"	       False	    2	    Move to next iteration
    2	   ("09:02", "ERROR", "Disk full")	 "ERROR"	    True	    3	    Return 

"""

def find_first_error(logs: list[tuple[str, str, str]]) -> tuple[tuple[int, tuple[str, str, str]] | None, int]:
    for index, entry in enumerate(logs):
        if entry[1] == "ERROR":
            return (index, entry), index + 1
    return None, len(logs)

