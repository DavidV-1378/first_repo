"""
WEEK 5 homework
Use: for-loops, if/elif/else, boolean ops, len/sum/max/min/sorted, set().
Avoid external libraries.
"""

# ======================================================================
# 1) CLINIC APPOINTMENT TRIAGE — conflicts + billing + doctor capacity
# ======================================================================
appointments = [
    # patient, doctor, start_min (since 09:00), duration_min, insurance (bool)
    {"patient": "Ava",   "doctor": "Dr. Pop",  "start":  0,  "dur": 30, "insured": True},
    {"patient": "Mihai", "doctor": "Dr. Pop",  "start": 25,  "dur": 30, "insured": False},  # conflict w/ Ava
    {"patient": "Ioan",  "doctor": "Dr. Ianc", "start": 60,  "dur": 45, "insured": True},
    {"patient": "Ana",   "doctor": "Dr. Pop",  "start": 70,  "dur": 20, "insured": True},
]

doctors = {
    # doctor: {end_min (since 09:00), base_fee, insured_discount_percent}
    "Dr. Pop":  {"end": 180, "fee": 200.0, "insured_disc": 30},
    "Dr. Ianc": {"end": 180, "fee": 180.0, "insured_disc": 20},
}

# Tasks:
# 1. Validate each appointment:
#    - Doctor exists, appointment ends before doctor's end, duration > 0.
#    - Check overlap conflicts PER DOCTOR (end = start + dur). Overlap => invalid with reason.
# 2. For valid ones, compute bill:
#    - fee = doctor fee; if insured, apply insured_disc% discount.
# 3. Per doctor: count valid appointments and total revenue. Also track invalid with reasons.
# 4. Print:
#    - Per-doctor schedule summary (count, revenue)
#    - Invalid appointments list with reasons.
# 5. Build a set of all patients that had conflicts.

# Hint: for overlap, keep a list of (start, end) per doctor; check if new interval intersects any.

# ======================================================================
# 2) SPORTS LEAGUE TABLE — points, tiebreakers, fair play
# ======================================================================
matches = [
    # home, away, home_goals, away_goals, home_cards, away_cards
    ("Wolves", "Hawks", 2, 2, 2, 3),
    ("Hawks",  "Lions", 1, 3, 1, 2),
    ("Lions",  "Wolves", 0, 1, 0, 1),
    ("Wolves", "Lions", 3, 3, 1, 0),
]

# Rules:
# - Win=3 pts, Draw=1 pt, Loss=0.
# - Track GF, GA, GD, Points, Cards (lower cards = better fair play).
# - Final table sorted by:
#     1) Points desc
#     2) Goal Difference desc
#     3) Goals For desc
#     4) Fair play asc (fewer cards is better)
# - Print a compact table.
# - Also print: top attack (max GF), stingiest defense (min GA).

table = {}  # team -> {"pts", "gf", "ga", "gd", "cards"}

# Hint: update both teams per match; compute gd at the end; use sorted(..., key=..., reverse=...)

# ======================================================================
# 3) ROAD TRIP FUEL & TIME PLANNER
# ======================================================================
car = {
    "tank_liters": 50,
    "consumption_l_per_100km": 7.2,
    "fuel_price_per_liter": 7.8,  # RON
    "avg_speed_kmh": 90
}

segments = [
    # name, distance_km
    ("Timisoara -> Deva", 155),
    ("Deva -> Alba Iulia", 60),
    ("Alba Iulia -> Turda", 70),
    ("Turda -> Cluj", 45),
]

budget_fuel = 400.0

# Tasks:
# 1. Compute total distance, driving time (hours), fuel needed (liters), fuel cost (RON).
# 2. If fuel needed > tank capacity, compute how many refuels (integer) are required
#    assuming you start full and refill only when needed (just report a count).
# 3. Boolean: within_fuel_budget?
# 4. Print a summary:
#    - total_distance, total_time (h), fuel_needed (L, 2 dec), fuel_cost (2 dec), refuels, budget status.

# Hint: fuel_needed = total_distance * consumption / 100

# ======================================================================
# 4) BACKUP & STORAGE PLANNER
# ======================================================================
files = [
    # filename, size_MB, checksum
    ("report1.pdf",   12, "aaa111"),
    ("photoA.jpg",   250, "bbb222"),
    ("video1.mp4",  2048, "ccc333"),
    ("photoA_copy.jpg", 250, "bbb222"),   # duplicate content (same checksum)
    ("dataset.zip",  3072, "ddd444"),
]

drives = {
    # drive label: capacity_MB
    "USB1": 4096,
    "USB2": 2048,
}

# Tasks:
# 1. Deduplicate by checksum: keep only the first occurrence of each checksum.
# 2. Compute total unique size. For each drive, boolean "fits_all" if all unique files fit.
# 3. If not "fits_all", compute how many MB overflow for that drive.
# 4. Print:
#    - kept files (names), removed duplicates count, total unique size
#    - per drive: capacity, fits_all, overflow(if any)

# Hint: like email dedup but keyed by checksum; sum sizes of kept files; loop over drives to compare.

# ======================================================================
# 5) AIRLINE BAGGAGE CHECK
# ======================================================================
passengers = [
    # name, bags(list of kg), ticket_tier, has_infant(bool)
    {"name": "Elena", "bags": [8, 18],      "tier": "ECONOMY", "infant": False},
    {"name": "Radu",  "bags": [10, 26],     "tier": "PREMIUM", "infant": True},
    {"name": "Iris",  "bags": [7, 21, 15],  "tier": "ECONOMY", "infant": False},  # extra bag
    {"name": "Mara",  "bags": [12],         "tier": "BUSINESS","infant": False},
]

allowances = {
    # tier: {max_bags, carry_on_kg, checked_kg}
    "ECONOMY":  {"max_bags": 2, "carry": 8,  "checked": 20},
    "PREMIUM":  {"max_bags": 2, "carry": 10, "checked": 23},
    "BUSINESS": {"max_bags": 2, "carry": 12, "checked": 32},
}
fees = {
    "extra_bag": 150.0,      # RON per extra beyond max_bags
    "over_carry_per_kg": 30.0,
    "over_checked_per_kg": 20.0,
    "infant_free_extra": True  # infant allows +1 small bag (<= 10kg) for free if exists
}

# Rules:
# - First bag is carry-on, remaining are checked.
# - If infant_free_extra and  the passenger has an infant and has more than max_bags: allow ONE extra bag <= 10kg without extra_bag fee (still charge weight overages if any).
# - Compute for each passenger:
#     * extra_bag_count (after infant rule)
#     * overweight fees: carry-on overage and sum of checked overage
#     * total_fees
# - Build a set "gate_flag" of names who pay more than 200 in feels or has any single bag larger than 32 kg
# - Print a per-passenger line and overall count of flagged passengers.

results = []
gate_flag = set()

# Hint: be careful to apply infant free extra BEFORE counting extra_bag fees.
#       Use max(0, weight - limit) for overages; sum checked separately.

