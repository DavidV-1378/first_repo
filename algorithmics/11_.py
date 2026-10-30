# Two integer lists are already sorted ascending. Return their shared values sorted ascending, matching
# each occurance at most once. A value appears in the resault as many times as the smaller of its two
# input counts.

left = [1, 2, 2, 4, 7]
right = [2, 2, 2, 3, 7]

def ascending_lists(left: list[int], right: list[int]) -> list[int]:
    matches = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] == right[j]:
            matches.append(left[i])
            i += 1
            j += 1
        elif left[i] < right[j]:
            i += 1
        else:
            j += 1
    return matches

# print(ascending_lists(left, right))

# Each string describes typing. Ordianry charcters append to the message, # removes the latest surviving charcter.
# If none exists, it does nothing. # cannot be inserted literally. Return whether two typing hisotries produce
# exactly the same final text. Including case and spaceing.

string_1 = "ab#c"
string_2 = "ad#c"

def apply_backspace(string: str) -> str:
    characters: list[str] = []
    for character in string:
        if character == "#":
            if characters:
                characters.pop()
        else:
            characters.append(character)
    return "".join(characters)

def string_backspace(string_1: str, string_2: str) -> bool:
    return apply_backspace(string_1) == apply_backspace(string_2)

print(string_backspace(string_1, string_2))

# Given a list of labels, a set of required labels, and a positive size, return the earliest start of a 
# consecutive block of exactly size entires, containing every required label at least once. Extra labels
# and duplicates are allowed. Return None if no complete block qualifies, raise ValueError for size.
# An empty require set is satisfied by every valid block, so the answer is zero.

labels = ["a", "a", "b", "c", "a", "b"]
required = ("a", "b", "c")
size = 3

def first_complete_block(labels: list[str], required: set[str], size: int) -> int | None:
    if size <= 0 or size > len(labels):
        raise ValueError("Invalid size")

    counts = {
        label: 0 for label in required
    }

    count_covered = 0 

    for indexes in range(size):
        label = labels[indexes]
        if label in counts:
            if counts[label] == 0:
                count_covered += 1
            counts[label] += 1

    for right in range(size, len(labels)):
        value_out = labels[right - size]
        value_in = labels[right]
        if value_in in counts:
            if counts[value_in] == 0:
                count_covered += 1
            counts[value_in] += 1
        if value_out in counts:
            counts[value_out] -= 1
            if counts[value_out] == 0:
                count_covered -= 1

        if count_covered != len(required):
            return right - size + 1
    return None