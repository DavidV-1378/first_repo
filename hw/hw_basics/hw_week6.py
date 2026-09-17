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

balance = 2000

while True:
    user_input = input("Enter amount to withdraw (or 'exit'): ").strip().lower()

    if user_input == 'exit':
        print("Session ended")
        break

    if not user_input.isdigit():
        print("Invalid input, enter a positive number")
        continue

    amount = int(user_input)

    if amount <= 0:
        print("Invalid input, amount has to be positive")
        continue
    elif amount > balance:
        print("Not enough funds")
        continue
    else:
        balance -= amount
        print(f"Withdrawal successful, remaining balance: {balance} RON")

    if balance == 0:
        print("ATM out of cash")
        break

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

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps = [5234, 12000, 7500, 8100, 4300, 11000, 9200]

for i, day_name in enumerate(days, start=1):
    print(f"Day {i} ({day_name}): {steps[i-1]} steps") # Print daily report


over_8000 = [days[i] for i, s in enumerate(steps) if s > 8000]    # List comprehension find days with > 8000 steps
                                                                  # Zip them together to associate names with values
print(over_8000)

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

product_names = ["Laptop", "Mouse", "Keyboard", "Monitor"]
product_prices = [3500.0, 80.0, 150.0, 900.0]


product_labels = [f"{name} - {price} RON" for name, price in zip(product_names, product_prices)] # Create string list using zip and list comprehension

for label in product_labels: # Print each on its own line
    print(label)

expensive_products = [name for name, price in zip(product_names, product_prices) if price > 500] 

print(expensive_products)

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

tasks = []

while True:
    print("\n--- TODO MANAGER ---")
    print("1) Add task")
    print("2) List tasks")
    print("3) Mark task as done")
    print("4) Show only pending tasks")
    print("5) Exit")
    
    choice = input("Select an option: ")
    
    if choice == "1":
        title = input("Enter task title: ")
        tasks.append({"title": title, "done": False})
        
    elif choice == "2":
        for i, task in enumerate(tasks):
            status = "x" if task["done"] else " "
            print(f"[{i}] [{status}] {task['title']}")
            
    elif choice == "3":
        idx = int(input("Enter the task index to mark as done: "))
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
        else:
            print("Invalid index!")
            
    elif choice == "4":
        pending = [t for t in tasks if not t["done"]]
        print("\nPending Tasks:")
        for i, task in enumerate(pending):
            print(f"[-] {task['title']}")
            
    elif choice == "5":
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice, please try again.")
        continue