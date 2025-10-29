"""
WEEK 3 — DATA STRUCTURES
---------------------------------------

Rules:
- No explicit loops (no for/while).
- Allowed: len, sum, max, min, sorted, tuple, list, set, membership ops (in/not in)
- Use indexing, slicing, tuple unpacking, set operations, list/dict methods.
- Simple if statements allowed only if unavoidable.

Goal:
Practice working with lists, tuples, sets, and dictionaries
using only built-in functions and operators — no iteration .
"""

# =========================================================
# YOUR DAILY BASKET (lists + dicts + sets)
# =========================================================

basket = [
    {"item": "bread", "price": 5.0, "category": "bakery"},
    {"item": "milk", "price": 6.5, "category": "dairy"},
    {"item": "apple", "price": 4.2, "category": "fruit"}
]

# TASKS:
# 1. Add a new item (same structure) to the basket.
# 2. Compute total cost (hint: use sum([...]) and explicit indices, no loop).
# 3. Build a set containing all unique categories.
# 4. Check if "meat" is in the categories set and store result in has_meat.
# 5. Create a tuple summary = (total_cost, len(basket)) and print all results.


# =========================================================
#  MOVIE INFO CARDS (dicts + tuples)
# =========================================================

movie1 = {
    "title": "Dune",
    "year": 2021,
    "genre": "Sci-Fi",
    "actors": ("Timothée Chalamet", "Zendaya")
}

# TASKS:
# 1. Add a new key "duration" = 155 to movie1.
# 2. Create another movie (same structure) named movie2 with your own values.
# 3. Store both in a list called movies.
# 4. Unpack the actors of movie1 into two variables.
# 5. Create a set containing the genres of both movies.
# 6. Compare durations and store the boolean in longer.
# 7. Print titles, durations, genres, and the comparison result.


# =========================================================
# MINI LIBRARY (dict of lists)
# =========================================================

library = {
    "borrowed": ["Dune", "The Hobbit"],
    "available": ["1984", "Brave New World", "Foundation"]
}

# TASKS:
# 1. Add "Harry Potter" to available books.
# 2. Move "1984" from available to borrowed using remove() and append().
# 3. Create a summary dict with:
#    - total_books = len(borrowed) + len(available)
#    - borrowed_count = len(borrowed)
# 4. Create a tuple stats = (borrowed_count, total_books).
# 5. Print the library, summary, and stats tuple.


# =========================================================
#  MUSIC SNAPSHOT (sets + dicts)
# =========================================================

rock = {"Queen", "The Beatles", "Coldplay"}
pop = {"Coldplay", "Adele", "Drake"}

#  TASKS:
# 1. Create both = artists in both sets.
# 2. Create all_artists = all unique artists (union).
# 3. Build a dict playlist_info with:
#    - total_artists = number of all unique artists
#    - common_artists = both
#    - unique_to_pop = artists only in pop
# 4. Print playlist_info and its values.


# =========================================================
#  WEEKEND PLAN (lists + tuples + sets + membership)
# =========================================================

my_activities = ["cinema", "gym", "reading"]
friend_activities = ["gym", "gaming", "cinema"]

#  TASKS:
# 1. Create sets: mine and friends from the lists.
# 2. Create a tuple weekend = (my first activity, friend’s last, total unique activities).
# 3. Check if "reading" is in my_activities and store result in quiet_time.
# 4. Print the weekend tuple and a message using quiet_time.


