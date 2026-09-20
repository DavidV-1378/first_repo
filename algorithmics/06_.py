# Sliding Windows

values = [4, 2, 7, 1, 8]
size = 3
# new_sum = old_sum - leaving_value + new_value

def fixed_window_sums(values: list[int], size: int) -> list[int]:
    if size <= 0 or size > len(values):
        raise ValueError("Invalid window size")
    current = 0
    results = []
    for index in range(size):
        current += values[index]
    results = [current]
    for right in range(size, len(values)):
        entering = values[right]
        leaving = values[right - size]
        current -= leaving 
        current += entering
        results.append(current)
    return results
    
# n values, k window size
# n - k + 1 = windows
# (n - k + 1) * k = additions
# complexity O(nk)
# sliding calculation = O(k) + O(n-k) = O(n)
# auxilliary sapce = O(1)

# Return the largest sum among all the windows of exactly size values.
values = [2, 1, 5, 1, 3, 2]
size = 3 

def max_windows_sum(values: list[int], size:int) -> int:
    if size <= 0 or size > len(values):
        raise ValueError("Invalid window size")
    current = 0
    for index in range(size):
        current += values[index]
    largest = current
    for right in range(size, len[values]):
        current += values[right] - values[right - size]
        if current > largest:
            largest = current
    return largest
    
# Return the starting index of every fixed sized window in which every sensor reading
# meets or exceeds a certain treshold.

values = [8.0, 9.0, 5.0, 10.0, 11.0, 12.0]
size = 3
treshold = 8.0

def sustained_alert_start(values: list[float], size: int, treshold: float) -> list[int]:
    if size <= 0 or size > len(values):
        raise ValueError("Invalid window size")
    count = 0
    starts = []
    for index in range(size):
        count += int(values[index] >= treshold)
    if count == size:
        starts.append(0)
    for right in range(size, len(values)):
        count += int(values[right] >= treshold) - int(values[right - size] >= treshold)
    if count == size:
        starts.append(right - size + 1)
    return starts