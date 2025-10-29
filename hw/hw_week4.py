"""
WEEK 4 Homework — Compound Data Structures, Conditionals, Boolean Expressions, For Loops
-------------------------------------------------------------------------------

- Use real-world thinking: validate inputs, compute summaries, and print clear results.
- You SHOULD use: for-loops, if/elif/else, boolean ops (and/or/not), len/sum/max/min/sorted, set().
- Avoid advanced libraries; stick to Python built-ins only.

"""

# ======================================================================
# 1) GROCERY ORDER CHECKER
# ======================================================================

order = [
    {"item": "milk",   "qty": 2, "unit_price": 6.5, "in_stock": True},
    {"item": "bread",  "qty": 1, "unit_price": 5.0, "in_stock": True},
    {"item": "steak",  "qty": 1, "unit_price": 35.0, "in_stock": False},
    {"item": "apples", "qty": 6, "unit_price": 1.8, "in_stock": True},
]
budget = 50.0

# Tasks:
# 1. Loop through the order and compute a subtotal BUT only include items that are in stock.
# 2. Collect the names of any items NOT in stock into a list: out_of_stock.
# 3. Check with a boolean expression if subtotal > budget and store in over_budget.
# 4. Print a small receipt:
#    - Subtotal (2 decimals)
#    - Out-of-stock items (list or "None")
#    - A line "Within budget" or "Over budget" based on over_budget.


# ======================================================================
# 2) CLASS ATTENDANCE & GRADES
# ======================================================================

students = [
    {"name": "Ana",   "present": True,  "grades": [9, 10, 8]},
    {"name": "Mihai", "present": False, "grades": [7, 8, 7]},
    {"name": "Ioana", "present": True,  "grades": [10, 9, 10]},
    {"name": "Dan",   "present": True,  "grades": [6, 7, 8]},
]
pass_threshold = 8.0

# Tasks:
# 1. For each student, compute the average grade and add it as "avg" (rounded to 2 decimals).
# 2. Add a "status" field with values "PASS" or "RETAKE" depending on the avg vs pass_threshold.
# 3. Count how many students are present today.
# 4. Build a list "needs_makeup" of students who are absent OR have status "RETAKE".
# 5. Print a mini report:
#    - Present count
#    - Each student: name, avg, status
#    - "Needs makeup": names list


# ======================================================================
# 3) STREAMING WATCHLIST FILTER
# ======================================================================

watchlist = [
    {"title": "Inception", "year": 2010, "rating": 8.8, "available": True,  "tags": ["mind-bend", "sci-fi"]},
    {"title": "Dune",      "year": 2021, "rating": 8.3, "available": True,  "tags": ["sci-fi", "epic"]},
    {"title": "Tenet",     "year": 2020, "rating": 7.4, "available": False, "tags": ["action", "time"]},
    {"title": "Amelie",    "year": 2001, "rating": 8.3, "available": True,  "tags": ["romance", "feelgood"]},
]
min_rating = 8.0
new_cutoff_year = 2015

# Tasks:
# 1. Build a new list "to_watch" with movies that are available and at least of min_rating
# 2. Split "to_watch" into two lists:
#       - "new_releases" for year after new_cutoff_year
#       - "classics"     for year before new_cutoff_year
# 3. Build a set "all_tags" that contains every unique tag from movies in "to_watch".
# 4. Print:
#       - Counts for to_watch/new_releases/classics
#       - all_tags
#       - The titles of new_releases and classics (nicely formatted)


# ======================================================================
# 4) EXPENSE CATEGORIZER
# ======================================================================

expenses = [
    {"desc": "Rent",        "amount": 1200, "category": "housing"},
    {"desc": "Groceries",   "amount": 280,  "category": "food"},
    {"desc": "Internet",    "amount": 45,   "category": "utilities"},
    {"desc": "Dining out",  "amount": 120,  "category": "food"},
    {"desc": "Gym",         "amount": 90,   "category": "health"},
]
monthly_budget = 1600
single_expense_limit = 500

# Tasks:
# 1. Compute total per category (build a dict: category -> sum).
# 2. Set a boolean "has_big_expense" if ANY single expense amount is larger than single_expense_limit.
# 3. Compute monthly_total and "over_budget" = monthly_total > monthly_budget.
# 4. Print a compact summary:
#       - category totals (dict)
#       - monthly_total (2 decimals)
#       - has_big_expense (True/False)
#       - "OK" or "Over budget" based on over_budget


# ======================================================================
# 5) CONTACTS DEDUPLICATOR
# ======================================================================

contacts = [
    {"name": "Alex", "email": "alex@example.com", "phone": "0711111111"},
    {"name": "Ana",  "email": "ana@example.com",  "phone": "0722222222"},
    {"name": "Alex", "email": "alex@example.com", "phone": "0799999999"},  # duplicate email
    {"name": "Mara", "email": "mara@example.com", "phone": "0733333333"},
]

# Tasks:
# 1. Use a set to track seen emails. Loop through contacts and build a new list "cleaned"
#    where you only keep the first contact for each unique email.
# 2. Count how many contacts were removed
# 3. Print:
#    - cleaned list
#    - removed_count


# ======================================================================
# CAPSTONE) MINI SHOP CART  (catalog + cart + validation + discounts)
# ======================================================================

catalog = {
    # sku: {name, price, stock}
    "MILK1L": {"name": "Milk 1L",         "price": 6.5,  "stock": 10},
    "BREAD":  {"name": "Bread",           "price": 5.0,  "stock": 4},
    "APPLE":  {"name": "Apple",           "price": 1.8,  "stock": 20},
    "COFFEE": {"name": "Coffee Beans 250g","price": 32.0, "stock": 3},
}

cart = [
    # sku, desired quantity
    {"sku": "MILK1L", "qty": 2},
    {"sku": "BREAD",  "qty": 1},
    {"sku": "APPLE",  "qty": 6},
    {"sku": "COFFEE", "qty": 2},   # try changing qty to test stock and discount rules
]

tax_rate = 0.09   # 9% VAT
coupon = {
    "code": "SAVE10",
    # apply 10% discount if (cart subtotal before tax) >= 60 OR if cart contains COFFEE with qty >= 2
    "type": "percent",
    "value": 10
}

# Tasks:
# 1. Validate items:
#    - For each cart line, check if sku exists in catalog AND qty <= stock.
#    - Build:
#        valid_lines: lines that pass validation
#        invalid_lines: lines that fail (missing sku OR qty > stock)
# 2. Compute line totals for valid_lines and a cart subtotal (before tax/discount).
# 3. Determine a boolean "coupon_applies" with this rule:
#       coupon applies if (subtotal >= 60) OR (exists a COFFEE line with qty >= 2).
# 4. If coupon_applies and coupon["type"] == "percent", compute discount_amount.
#    Else discount_amount = 0.
# 5. Compute tax on (subtotal - discount_amount), then final_total.
# 6. Print a clean receipt:
#      - Each valid line: name, qty, unit price, line total
#      - Subtotal
#      - Discount (if any) with the code
#      - Tax
#      - FINAL TOTAL
#      - If there are invalid_lines, print them clearly with the reason.
# 7. OPTIONAL: After successful “checkout”, reduce catalog stock by qty for each valid line and print updated stock.
