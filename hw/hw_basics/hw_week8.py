"""
HOMEWORK — Exceptions, Iterators, Generators
--------------------------------------------
Write clear, readable code and add small comments where it helps.
"""

# ======================================================================
# 1) EXCEPTIONS — APPOINTMENT BOOKING VALIDATOR
# ======================================================================
"""
You are building a small helper for a clinic’s appointment system.

A valid appointment duration must:
- be an integer
- be between 15 and 120 minutes (inclusive)

Requirements:
1. Write a function parse_duration(raw: str) -> int | None that:
   - tries to convert raw (a string) to int
   - if conversion fails, prints a message and returns None
   - if the value is outside [15, 120], raises a ValueError with a clear message
   - otherwise returns the integer value

2. In a small demo section:
   - ask the user for a string using input("Enter duration in minutes: ")
   - call parse_duration on it inside a try/except block
   - if a ValueError is raised, catch it and print:
         "Invalid duration:", error_message
   - if the function returns None, print:
         "Could not parse duration."
   - if everything is fine, print:
         "Appointment booked for X minutes."

IMPORTANT:
- Practice both: returning None and raising ValueError.
- Do NOT catch exceptions inside parse_duration for the out-of-range case.
"""

# Your code here for Problem 1

def parse_duration(raw: str) -> int | None:
   try:
      value = int(raw)
      if not 15 <= value <= 120:
         raise ValueError(f"value {value} is out of range.")
      return value
   except ValueError as e:
      print(f"Converison failed {e}")
      return None
        
# demo section

appointment = input("Enter duration in minutes:")

try:
    duration = parse_duration(appointment)
    print(f"Parsed successfully: {duration}")
except ValueError as e:
    print(f"Failed to prase duration: {e}")
    duration = None

# ======================================================================
# 2) ITERATORS — LOG READER
# ======================================================================
"""
You are analyzing a very small system log stored as a list of strings:

logs = [
    "INFO: System started",
    "WARNING: High memory usage",
    "ERROR: Disk almost full",
    "INFO: Cleanup started",
    "ERROR: Cleanup failed",
]

Requirements:
1. Create the logs list exactly as above.

2. Use iter(logs) to create an iterator object log_iter.
   - Do NOT use a for-loop yet.
   - Use next to print the first TWO entries.

3. Now use a for-loop over the SAME iterator (not a new one) to print
   the remaining log entries, each prefixed with its index:
      "[0] INFO: ..."
      "[1] WARNING: ..."

   DO NOT FORGET THE INDEX!

4. After the iterator is exhausted, call next(log_iter) once more
   inside a try/except block and:
   - if StopIteration is raised, print:
        "End of log reached."
"""

# Your code here for Problem 2

logs = [
    "INFO: System started",
    "WARNING: High memory usage",
    "ERROR: Disk almost full",
    "INFO: Cleanup started",
    "ERROR: Cleanup failed",
]

log_iter = iter(logs)

print(next(log_iter))
print(next(log_iter))

for index, log in enumerate(log_iter, start=2):
    print(f"[{index}] {log}")

# ======================================================================
# 3) GENERATORS — ALERT STREAM FOR SENSOR VALUES
# ======================================================================
"""
You have sensor readings that measure temperature in °C.
You want to classify each reading into three categories:

- below 0°C   -> ("FREEZING", value)
- 0–30°C      -> ("NORMAL", value)
- above 30°C  -> ("OVERHEAT", value)

Requirements:
1. Write a generator function classify_temperatures(values) that:
   - takes a list of numeric values
   - yields a tuple (status, value) according to the rules above

2. In a small demo:
   - create a list temps = [-5, 0, 10, 31, 45]
   - iterate over classify_temperatures(temps) 
   - print human-readable messages such as:
        "Reading -5°C -> FREEZING"
        "Reading 10°C -> NORMAL"
        "Reading 31°C -> OVERHEAT"

   Add a docstring to classify_temperatures explaining that it is
   a generator, what it yields, and what the input is.
"""

# Your code here for Problem 3

from typing import Generator, Tuple, Iterable

temperatures = [-5, 0, 10, 31, 45]

def classify_temperature(values: Iterable[float]) -> Generator[Tuple[str, float], None, None]:
    for value in values:
         if value < 0:
            yield ("FREEZING", value)
         elif value <= 30:
            yield ("NORMAL", value)
         else:
            yield ("OVERHEAT", value)

"""gen = classify_temperature(temperatures) 
status, temp_value = next(gen)
print(f"Reading {temp_value} -> {status}")
status, temp_value = next(gen)
print(f"Reading {temp_value} -> {status}")
status, temp_value = next(gen)
print(f"Reading {temp_value} -> {status}")"""

for status, temp_value in classify_temperature(temperatures):
   print(f"Reading {temp_value} -> {status}")


# ======================================================================
# 4) ORDER PROCESSING PIPELINE
# ======================================================================
"""
You are simulating a very small e-commerce order processing pipeline.

Each raw order is represented as a dictionary, for example:
    {"id": "A01", "quantity": "3", "price": "19.99"}
    {"id": "A02", "quantity": "X", "price": "5.00"}   # invalid quantity
    {"id": "A03", "quantity": "2", "price": "abc"}    # invalid price

Requirements:

1) DATA SETUP
-------------
Create a list raw_orders with at least 5 such dictionaries.
Include:
- at least one valid order
- at least one with invalid quantity
- at least one with invalid price
- at least one with quantity <= 0 (also invalid)

2) VALIDATION FUNCTION (exceptions)
-----------------------------------
Write a function parse_order(order: dict) -> dict that:
- Tries to convert:
    quantity_str = order["quantity"]
    price_str = order["price"]
  into:
    quantity: int
    price: float
- If conversion fails for either field, raises ValueError with a clear message.
- If quantity <= 0, also raises ValueError.
- If all is OK, returns a NEW dictionary:
    {
        "id": <same as input>,
        "quantity": <int>,
        "price": <float>,
        "total": quantity * price
    }

Do NOT catch exceptions inside parse_order.

3) GENERATOR FOR VALID ORDERS
------------------------------
Write a generator function valid_orders(raw_orders) that:
- takes the list of raw_orders
- for each raw order:
    - tries to parse it using parse_order
    - if parse_order raises ValueError, print a message like:
          "Skipping invalid order <id>: <error message>"
      and SKIP that order (do not yield anything)
    - if parsing succeeds, yield the cleaned order dictionary

4) ITERATOR USAGE & STATISTICS
------------------------------
In a final demo section:

a) Create an iterator from the generator:
b) Use next(it) once
c) Then use a for-loop on the SAME iterator to process remaining orders:
   - accumulate the sum of all order["total"]
   - count how many valid orders were processed
   - at the end print:
        "Processed N valid orders, total revenue: X RON"
d) Wrap the initial next(it) in try/except StopIteration to handle the
   case where there are ZERO valid orders. If that happens, print:
        "No valid orders found."
"""

# Your code here for Problem 4

raw_orders: list[dict[str, str]] = [
    {"id": "A01", "quantity": "3", "price": "19.99"},
    {"id": "A02", "quantity": "X", "price": "5.00"},   
    {"id": "A03", "quantity": "2", "price": "abc"},
    {"id": "A04", "quantity": "0", "price": "14.99"},
    {"id": "A05", "quantity": "-1", "price": "24.99"}
]

def parse_order(order: dict[str, str]) -> dict[str, object]:
    quantity_str = order["quantity"] 
    price_str = order["price"]
    try:
        quantity: int = int(quantity_str)
    except ValueError as e:
        raise ValueError(f"Invalid Quantity {quantity_str} must be int") from e
    try:
        price: float = float(price_str)
    except ValueError as e:
        raise ValueError(f"Invalid price {price_str} must be a float") from e
    if quantity <= 0:
        raise ValueError(f"Invalid quantity {quantity}, quantity must be > 0")
    
    total = price * quantity
    
    return {
        "id":order["id"],
        "quantity": quantity,
        "price": price,
        "total": total
    }

def valid_orders(raw_orders: Iterable[dict[str, str]]) -> Generator[dict[str, object], None, None]:
   for raw_order in raw_orders:
      
      id = raw_order.get("id", "missing")
      
      try:
         cleaned_order = parse_order(raw_order)
      except ValueError as e:
          print(f"Skipping invalid order {id}: {e}")
          continue
      yield cleaned_order  

count_valid_orders: int = 0

total_revenue: float = 0.0

it = valid_orders(raw_orders)

try:
   first = next(it)
except StopIteration:
    print("No valid orders found.")
else:
    count_valid_orders += 1
    total_revenue += float(first["total"])

for order in it:
    total_revenue += float(order["total"])
    count_valid_orders += 1

print(f"Processed {count_valid_orders} valid orders, total revenue: {total_revenue:.2f} RON")