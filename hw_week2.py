# Week 2 — Homework: Operators, Data Types,  Lists
# ---------------------------------------------------
# Instructions:
# - Solve each exercise directly below its statement.
# - Use ONLY what we covered so far: numbers, strings, booleans, basic operators,
#   and LISTS (indexing, slicing, append, insert, remove/pop, membership, count, etc.).
# - You can print results to verify. Keep your code clean and readable.
# - OPTIONAL: If you want, wrap solutions in small functions, but not required.

print("=== Week 2 Homework: Operators, Data Types, and Lists ===")

# ---------------------------------------------------
# EXERCISE 1 (easy) — Basic numeric operators
#You’re packing snack bars into boxes.
#Input (hardcode for now): bars = 47, per_box = 6.
#Compute and print:
#How many full boxes you can make
#How many leftover bars
# How many extra bars you need to buy to complete the last box
#----------------------------------------------------


# ---------------------------------------------------
# EXERCISE 2 (easy) — String basics and indexing
# Generate a fun user handle from a name.
# Given full_name = "Ada Lovelace" (or his own):
# Lowercase, remove spaces.
# Make handle = first 3 letters + last 2 letters reversed.
# Count the number of vowels in the original name (membership: in "aeiouAEIOU").
# Print: handle + “-” + vowel_count.

# ---------------------------------------------------
# EXERCISE 3  — Lists: create, index, slice, modify
# A small bus has 10 seats. "X" means taken, "_" means free.
# Start: seats = ["_", "X", "_", "_", "X", "_", "_", "_", "X", "_"]
# Tasks:
# Print total seats, how many free and first/last seat states.
# A group of 2 arrives; reserve two consecutive free seats by scanning the list and replacing with "X"
# A passenger leaves from the last occupied seat
# Print the list after each step.

# ---------------------------------------------------
# EXERCISE 4 List membership & methods
# Edit a tiny playlist (just titles as strings).
# Start: playlist = ["Flowers", "Thunder", "Daylight", "River", "Waves"]
# Tasks:
# Insert "Intro" at the start, append "Outro" at the end.
# If "Thunder" exists, move it to the end (remove then append).
# Print the middle slice (exclude first and last) as the “core set.”
# Check if "Silence" is in the playlist (membership) and print result.


# ---------------------------------------------------
# EXERCISE 5  — Clean a list & compute a score
# You receive a messy list of "scores" as strings/ints with duplicates and invalid values.
# Start from: raw = ["10", 5, "x", 5, " 20", "12", "x", 20, "20", "7 "]
# Tasks:
# 1) Build a new list valid_scores (ints only) by:
# Converting numeric-looking strings to int )
# Keeping ints as-is
# Skipping invalid entries ("x", anything not a proper int)
# 2) Remove duplicates *while preserving the first occurrence order (use only lists).
# 3) Compute:
#   - count (how many items)
#   - total sum
#   - average (float); if empty, average is 0.0
# 4) Print the cleaned list and the three numbers.
#
