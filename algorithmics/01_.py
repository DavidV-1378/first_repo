values = [4, 7, 2]
total = 0
for value in values:
    total += value
print(total)

# 1. Given a list of temperatures, return the first temperature above 30. If none is above 30, return None.

[26, 28, 31]
[27, 29, 30]
[]

def first_temperature_above_thirty(temperatures: list[int]) -> int | None:
    for temperature in temperatures:
        if temperature > 30:
            return temperature
    return None

def largest(values: list[int]) -> int:
    best = values[0]
    for value in values[1:]:
        if value > best:
            best = value
    return best

# state: information currently stored while an algorithm is running
# trace: a written record of how the state changes

def count_negative(values: list[int]) -> int:
    count = 0
    for value in values:
        if value < 0:
            count += 1
    return count
    

[3, -1, -5, 2] 
# 0: 0, 1: 0, 2: 1, 3: 2, 4: 2, result: 2

def string_contains_number(string: str) -> bool:
    for char in string:
        if char.isdigit():
            return True
    return False

# "word word 1 word" = True
# "word word word" = False
# "1" = True
# "" = False

# Given a list of submission statuses, return the index of the first accepted submission.
# Return None if none are accepted

# ["rejected", "rejected", "accepted"] = 2
# ["rejected", "rejected"] = None
# [] = None

def frist_accepted_submission_status(submission_statuses: list[str]) -> int | None:
    for index, status in enumerate(submission_statuses):
        if status == "accepted":
            return index
    return None

#TODO: trace values

# Each reading is (sensor_id, value). Return the first readings below 0 or above 100. Othewise, return None.

def first_invalid_reading(readings: list[tuple[str, int]]) -> tuple[str, int] | None:
    for reading in readings:
        _, value = reading
        if value < 0 or value > 100:
            return reading
    return None