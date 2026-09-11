# Given a sorted list with at least two values, return the pair whose sum is closest to the target.

values = [1, 4, 6, 8, 15]
target = 13

def closest_to_target(values: list[int], target: int) -> tuple[int, int]:
    if len(values) < 2:
        raise ValueError("List must have at least two values")
    left = 0
    right = len(values) - 1
    best = (values[left], values[right])
    while left < right:
        current = values[left] + values[right]
        current_distance = abs(current - target)
        best_sum = best[0] + best[1]
        best_distance = abs(best_sum - target)
        if current_distance < best_distance:
            best = (values[left], values[right])
        if current_distance > target:
            right -= 1
        elif current_distance < target:
            left += 1
        else:
            return best
    return best
        
        
        
# left = 1, right = 15 cd = 3, bd = 3 best = 1, 15
# left = 1, right = 8 cd = 4, bd = 3 best = 1, 15
# left = 4 right = 8, cd = 1 bd = 1 best = 4, 8
# left = 6 right = 8, cd = 1, bd = 1, best = 4, 8


# Merge sorted sequences
left_values = [1, 4, 7]
right_values = [2, 4, 9, 10]

def merge_sorted_sequences(left_values: list[int], right_values: list[int]) -> list[int]:
    merged_values = []
    left = 0
    right = 0
    while (left < len(left_values) and right < len(right_values)):
        if left_values[left] <= right_values[right]:
            merged_values.append(left_values[left])
            left += 1
        else
            merged_values.append(right_values[right])
            right += 1
    while right < len(right_values):
        merged_values.append(right_values[right])
        right += 1
    while left < len(left_values):
        merged_values.append(left_values[left])
        left += 1
    return merged_values