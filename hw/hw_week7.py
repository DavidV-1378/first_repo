"""
HOMEWORK — Functions, parameters, scope, lambda, documentation
---------------------------------------------------------------

- write functions with good parameters and return values
- use named and default parameters
- understand basic scope (local vs outer)
- use lambda functions where appropriate
- write simple, meaningful docstrings
"""

# ======================================================================
# 1) TEMPERATURE CONVERTER SERVICE (functions + docstrings)
# ======================================================================
"""
You are implementing a tiny temperature conversion microservice.

Requirements:
1. Write a function c_to_f(celsius: float) -> float
   that converts °C to °F using the formula:
        F = C * 9/5 + 32
2. Write a function f_to_c(fahrenheit: float) -> float
   that converts °F to °C.
3. Add clear DOCSTRINGS to both functions explaining what
   they do, their parameters and return values.
4. Ask the user for:
     - a temperature value
     - a direction ("CtoF" or "FtoC")
   then call the correct function and print the result.
"""

# Your code here


# ======================================================================
# 2) ONLINE SHOPPING CART (functions + default & named params)
# ======================================================================
"""
You are modeling the backend logic for a shopping cart.

Each item in the cart is a dictionary:
   {"name": "Book", "price": 35.0, "qty": 2}

Requirements:
1. Create a list cart with at least 3 such items.
2. Write a function compute_total that akes cart, tax_rate=0.19, and discount=0.0 as params 
   that:
   - computes the subtotal 
   - applies discount as a fraction 
   - applies tax on the discounted value
   - RETURNS the final total.
3. Add a docstring explaining parameters (including defaults).
4. Call compute_total in at least 3 ways:
   - only with the cart (tax_rate and discount default)
   - with a custom discount using a named parameter
   - with both custom tax_rate and discount using named parameters.
5. Print each returned total with a label.
"""

# Your code here




# ======================================================================
# 3) SHORT TEXT ANALYTICS (functions + return values + lambda)
# ======================================================================
"""
You are building a small text analytics helper.

Requirements:
1. Write a function text_stats(text: str) -> dict that returns:
     {
       "length": number_of_characters,
       "words": number_of_words,
       "avg_word_length": average_length_of_words
     }
   (You can define "word" as split on spaces.)
2. Add a docstring.
3. Write a second function top_n_words_by_length(text: str, n: int)
   that:
   - splits the text into words
   - removes empty strings
   - uses sorted + a LAMBDA function as key to sort words by length (descending)
   - returns the first n words.
4. Use both functions on a sample text, print the stats and the top 3 words.
"""

# Your code here




# ======================================================================
# 4) SIMPLE COUNTER — SCOPE AND SIDE EFFECTS
# ======================================================================
"""
You are simulating a request counter.  
We want to understand scope and avoid weird bugs.

Requirements:
1. Create a function make_counter(start=0) that:
   - uses an INNER (nested) function increment()
   - increment() increases a variable stored in the enclosing scope
     (nonlocal) and RETURNS the new value.
   - make_counter RETURNS the increment function.
2. Create two independent counters:
      c1 = make_counter()
      c2 = make_counter(100)
3. Call c1() three times and print the results.
4. Call c2() two times and print the results.
5. Make sure that c1 and c2 DO NOT interfere with each other.
6. Add docstrings to explain what make_counter returns and how it works.
"""

# Your code here




# ======================================================================
# 5) FINAL CHALLENGE — STUDENT GRADEBOOK SERVICE
# functions + scope (passing data) + lambda + documentation
# ======================================================================
"""
You are implementing the core logic for a "student gradebook" API.

We represent the gradebook as a list of dictionaries:
  students = [
      {"name": "Ana", "grades": [9, 10, 8]},
      {"name": "Mihai", "grades": [7, 6]},
      ...
  ]

Requirements:
1. Write a function add_student(students, name: str) -> None
   that adds a new student with an empty grades list IF the
   name does not already exist.
   (No return value needed; it modifies the list passed in.)

2. Write a function add_grade(students, name: str, grade: int) -> bool
   that:
   - finds the correct student
   - appends the grade
   - returns True if it succeeded, False if student not found.

3. Write a pure function average(grades: list[int]) -> float
   that:
   - returns 0 if the list is empty
   - otherwise returns the arithmetic mean.

4. Write a function compute_averages(students) -> dict
   that returns a dictionary:
     { "Ana": 9.0, "Mihai": 6.5, ... }

5. Write a function top_students(students, n: int = 3) -> list[tuple[str, float]]
   that:
   - uses compute_averages
   - turns the result into a list of (name, avg) tuples
   - uses sorted + LAMBDA to sort them by avg descending
   - returns the first n tuples.

6. Add short docstrings to the main functions.

7. In a small demo section at the bottom:
   - create an empty students list
   - add 3–4 students and some grades
   - print all averages
   - print the top 2 students with their averages.
"""

# Your code here
