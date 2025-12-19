"""
HOMEWORK — While loops, list comprehensions, enumerate, zip, break, continue
----------------------------------------------------------------------------

Write clean, readable code and add small comments where needed.
"""

# ======================================================================
# 1) ATM CASH WITHDRAWAL SIMULATOR (while + break + continue)
# ======================================================================
"""
You are simulating how an ATM handles cash withdrawals.

Requirements:
1. Start with a variable balance = 2000 (RON).
2. Use a WHILE loop that repeatedly asks:
       "Enter amount to withdraw (or 'exit'): "
3. If the user types "exit":
       - print "Session ended." and break.
4. If the amount is NOT a positive integer:
       - print "Invalid input." and continue (skip this round).
5. If the amount is greater than the current balance:
       - print "Insufficient funds." and continue.
6. Otherwise:
       - subtract it from the balance,
       - print "Withdrawal successful. Remaining balance: X".
7. If the balance reaches 0:
       - print "ATM is out of cash." and stop the loop (break).
"""

# Your code here


# ======================================================================
# 2) CLEANING UP USER INPUT (while + continue)
# ======================================================================
"""
You are collecting tags for a blog post.  
The user can type tags one by one. Some inputs are invalid and must be skipped.

Requirements:
1. Use a while True loop to repeatedly ask:
      "Enter a tag (or 'done' to finish): "
2. If the user types "done" (any case, e.g. "Done", "DONE"):
      - stop the loop with break.
3. If the user enters an empty string or only spaces:
      - ignore it and continue (use continue).
4. Store all valid tags in a list.
5. At the end print:
      "You entered N tags: [ ... ]"
"""

# Your code here




# ======================================================================
# 3) STEP TRACKER (list comprehensions + enumerate)
# ======================================================================
"""
A fitness app stores the number of steps for each day of the week.

Requirements:
1. Create a list days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"].
2. Create a list steps with 7 integers (fake data), one for each day.
3. Use enumerate to print them as:
      "Day 1 (Mon): 5234 steps"
      "Day 2 (Tue): ...."
4. Use a LIST COMPREHENSION to build a new list over_8000
      containing only the days where steps > 8000.
      Hint: you may want a list of day names or of (day, steps) tuples.
5. Print the over_8000 list in a readable way.
"""

# Your code here


# ======================================================================
# 4) MERGING PRODUCT DATA (zip + list comprehensions)
# ======================================================================
"""
You get separate lists from two different microservices:

  product_names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
  product_prices = [3500.0, 80.0, 150.0, 900.0]

Requirements:
1. Create the two lists above.
2. Use zip to combine them into pairs: ("Laptop", 3500.0), etc.
3. Using a list comprehension, build a list of strings like:
      "Laptop - 3500.0 RON"
4. Print each line on its own line.
5. Using ANOTHER list comprehension, extract only the products
   that cost more than 500 RON into a list expensive_products.
   Print them.
"""

# Your code here


# ======================================================================
# 5) SIMPLE TODO MANAGER
# while + break/continue + list comprehensions + enumerate
# ======================================================================
"""
You are building a very small command-line TODO manager.

Each task is stored as a dictionary:
   {"title": "Buy milk", "done": False}

Requirements:
1. Start with an empty list tasks = [].
2. Use while True to show a text menu:

   1) Add task
   2) List tasks
   3) Mark task as done
   4) Show only pending tasks
   5) Exit

3. Option 1: ask the user for a task title and append a new dict.
4. Option 2: list ALL tasks using enumerate, as:
      [0] [ ] Buy milk
      [1] [x] Pay bills
   where [ ] means not done, [x] means done.
5. Option 3: ask for the task INDEX, check it's valid,
   and mark that task as done.
6. Option 4: use a LIST COMPREHENSION to build a list of only
   pending tasks and display them similarly.
7. Option 5: exit the program (use break).
8. For invalid menu choices, print a message and continue.
"""
# Your code here