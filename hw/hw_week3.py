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

# TASKS:
# 1. Add a new item (same structure) to the basket.
# 2. Compute total cost (hint: use sum([...]) and explicit indices, no loop).
# 3. Build a set containing all unique categories.
# 4. Check if "meat" is in the categories set and store result in has_meat.
# 5. Create a tuple summary = (total_cost, len(basket)) and print all results.

basket = [
    {"item": "bread", "price": 5.0, "category": "bakery"},
    {"item": "milk", "price": 6.5, "category": "dairy"},
    {"item": "apple", "price": 4.2, "category": "fruit"}
]

basket.append({"item": "potatoes", "price": 5.4, "category": "vegetables"})

total_cost = sum([
    basket[0]["price"],
    basket[1]["price"],
    basket[2]["price"],
    basket[3]["price"]
])

categories = set([
    basket[0]["category"],
    basket[1]["category"],
    basket[2]["category"],
    basket[3]["category"]
])

has_meat = "meat" in categories

summary = (total_cost, len(basket))

print("Basket:", basket)
print("Total cost:", total_cost)
print("Categories:", categories)
print("Has meat:", has_meat)
print("Summary (total_cost, number_of_items):", summary)

# =========================================================
#  MOVIE INFO CARDS (dicts + tuples)
# =========================================================

# TASKS:
# 1. Add a new key "duration" = 155 to movie1.
# 2. Create another movie (same structure) named movie2 with your own values.
# 3. Store both in a list called movies.
# 4. Unpack the actors of movie1 into two variables.
# 5. Create a set containing the genres of both movies.
# 6. Compare durations and store the boolean in longer.
# 7. Print titles, durations, genres, and the comparison result.

movie1 = {
    "title": "Dune",
    "year": 2021,
    "genre": "Sci-Fi",
    "actors": ("Timothée Chalamet", "Zendaya")
}

movie1["duration"] = 155

movie2 = {
    "title": "Avatar: The Way of Water",
    "year": 2022,
    "genre": "Action",
    "actors": ("Sam Worthington", "Zoe Saldana"),
    "duration": 192
}

movies = [movie1, movie2]

actor1, actor2 = movie1["actors"]

genres = set([movie1["genre"], movie2["genre"]])

longer = movie1["duration"] > movie2["duration"]

print("Movie 1 Title:", movie1["title"])
print("Movie 1 Duration:", movie1["duration"], "minutes")
print("Movie 2 Title:", movie2["title"])
print("Movie 2 Duration:", movie2["duration"], "minutes")
print("Genres:", genres)
print("Actors from Movie 1:", actor1, "and", actor2)
print("Is Movie 1 longer than Movie 2?", longer)

# =========================================================
# MINI LIBRARY (dict of lists)
# =========================================================

# TASKS:
# 1. Add "Harry Potter" to available books.
# 2. Move "1984" from available to borrowed using remove() and append().
# 3. Create a summary dict with:
#    - total_books = len(borrowed) + len(available)
#    - borrowed_count = len(borrowed)
# 4. Create a tuple stats = (borrowed_count, total_books).
# 5. Print the library, summary, and stats tuple.

library = {
    "borrowed": ["Dune", "The Hobbit"],
    "available": ["1984", "Brave New World", "Foundation"]
}

library["available"].append("Harry Potter")

library["available"].remove("1984")
library["borrowed"].append("1984")

summary = {
    "total_books": len(library["borrowed"]) + len(library["available"]),
    "borrowed_count": len(library["borrowed"])
}

stats = (summary["borrowed_count"], summary ["total_books"])

print("Library:", library)
print("Summary:", summary)
print("Stats:", stats)

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

rock = {"Queen", "The Beatles", "Coldplay"}
pop = {"Coldplay", "Adele", "Drake"}

both = rock and pop
all_artists = rock | pop

playlist_info = {
    "total_artists": len(all_artists),
    "common_artists": both,
    "unique_to_pop": pop - rock
}

print("Playlist Info:", playlist_info)
print("Total artists:", playlist_info["total_artists"])
print("Common artists:", playlist_info["common_artists"])
print("Unique to pop:", playlist_info["unique_to_pop"])


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


