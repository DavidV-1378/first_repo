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

