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


valid_appointments = [] #list of valid appointments
invalid_appointments = [] #list of invalid appointments 
doctor_stats = {doctor: {"count": 0, "revenue": 0.0, "intervals": []} for doctor in doctors} #informtaion of doctor
time_conflict_patients = set() #patients with time conflicts

for appointment in appointments:  # go through each appointment in the list
    patient = appointment["patient"]
    doctor = appointment["doctor"]
    start = appointment["start"]
    dur = appointment["dur"]
    insured = appointment["insured"]

    if doctor not in doctors:  # check if doctor name is valid
        invalid_appointments.append((patient, doctor, "Unknown doctor"))
        continue  # skip to next appointment
    if dur <= 0:  # check if duration is positive
        invalid_appointments.append((patient, doctor, "Invalid duration"))
        continue  # skip to next appointment

    end = start + dur  # calculate end time
    if end > doctors[doctor]["end"]:  # check if appointment goes beyond doctor's working time
        invalid_appointments.append((patient, doctor, "Exceeds doctor time"))
        continue  # skip to next appointment

    conflict = False  # assume no conflict first
    for (s, e) in doctor_stats[doctor]["intervals"]:  # go through each existing (start,end) for that doctor
        if start < e and end > s:  # if times overlap, there is a conflict
            conflict = True
            break  # stop checking more intervals
    if conflict:  # if there was an overlap
        invalid_appointments.append((patient, doctor, "Time conflict"))
        time_conflict_patients.add(patient)  # record patient in conflict list
        continue  # skip to next appointment

    doctor_stats[doctor]["intervals"].append((start, end))  # save new appointment time for doctor

    fee = doctors[doctor]["fee"]  # base fee
    if insured:  # if the patient has insurance
        disc = doctors[doctor]["insured_disc"]
        fee = fee * (1 - disc / 100)  # apply discount

    doctor_stats[doctor]["count"] += 1  # add one valid appointment
    doctor_stats[doctor]["revenue"] += fee  # add the fee
    valid_appointments.append((patient, doctor, fee))  # store result

for doc in sorted(doctor_stats):  # go through doctors in alphabetical order
    c = doctor_stats[doc]["count"]
    rev = doctor_stats[doc]["revenue"]
    print(f"{doc}: {c} valid appointment(s), total revenue = {rev:.2f}")

for pat, doc, reason in invalid_appointments:  # go through all invalid ones
    print(f"{pat} ({doc}) → {reason}")

print(sorted(time_conflict_patients))  # show all conflict patients alphabetically

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

for home, away, hg, ag, hc, ac in matches:  # go through each match in the list
    # add both teams if not yet in table
    if home not in table:  # check if home team is new
        table[home] = {"pts": 0, "gf": 0, "ga": 0, "gd": 0, "cards": 0}
    if away not in table:  # check if away team is new
        table[away] = {"pts": 0, "gf": 0, "ga": 0, "gd": 0, "cards": 0}

    table[home]["gf"] += hg  # add goals scored by home
    table[home]["ga"] += ag  # add goals conceded by home
    table[away]["gf"] += ag  # add goals scored by away
    table[away]["ga"] += hg  # add goals conceded by away
    table[home]["cards"] += hc  # add cards for home
    table[away]["cards"] += ac  # add cards for away

    if hg > ag:  # if home team scored more
        table[home]["pts"] += 3
    elif hg < ag:  # if away team scored more
        table[away]["pts"] += 3
    else:  # if same number of goals
        table[home]["pts"] += 1
        table[away]["pts"] += 1

for team in table:  # go through every team in the table
    table[team]["gd"] = table[team]["gf"] - table[team]["ga"]

# sort teams according to rules
sorted_teams = sorted(
    table.items(),
    key=lambda t: (t[1]["pts"], t[1]["gd"], t[1]["gf"], -t[1]["cards"]),
    reverse=True,  
)

print("Team       Pts  GF  GA  GD  Cards") # print league table
for team, stats in sorted_teams:  # print each team and their stats
    print(f"{team:<10} {stats['pts']:>3}  {stats['gf']:>2}  {stats['ga']:>2}  {stats['gd']:>3}  {stats['cards']:>3}")

# find top attack and best defense
max_gf = -1
best_attack = ""
min_ga = 9999
best_defense = ""

for team, stats in table.items():  # go through all teams to find max GF and min GA
    if stats["gf"] > max_gf:  # check if this team has more goals 
        max_gf = stats["gf"]
        best_attack = team
    if stats["ga"] < min_ga:  # check if this team has fewer goals 
        min_ga = stats["ga"]
        best_defense = team

print("Top attack:", best_attack, f"({max_gf} GF)")
print("Best defense:", best_defense, f"({min_ga} GA)")



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


total_distance = 0 # compute total distance
for name, dist in segments:  # go through each trip segment
    total_distance += dist  # add the distance of the segment

# compute total driving time 
total_time = total_distance / car["avg_speed_kmh"]  # time = distance / speed

# compute fuel needed 
fuel_needed = total_distance * car["consumption_l_per_100km"] / 100  # liters needed

# compute total fuel cost
fuel_cost = fuel_needed * car["fuel_price_per_liter"]  # RON

# compute number of refuels
if fuel_needed <= car["tank_liters"]:  # if total fuel fits in one tank
    refuels = 0  # no refuel needed
else:  # otherwise need to refill
    refuels = int(fuel_needed // car["tank_liters"])  # count full refuels
    if fuel_needed % car["tank_liters"] > 0:  # if there's leftover distance needing partial refill
        refuels += 1  # add one more refill

# check if within fuel budget
if fuel_cost <= budget_fuel:  # if cost is under or equal to budget
    within_budget = True
else:  # if cost exceeds budget
    within_budget = False

print(f"Total distance: {total_distance} km")
print(f"Total driving time: {total_time:.2f} hours")
print(f"Fuel needed: {fuel_needed:.2f} liters")
print(f"Fuel cost: {fuel_cost:.2f} RON")
print(f"Refuels required: {refuels}")
print(f"Within budget: {within_budget}")

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


unique_files = []  # will store only unique files
seen_checksums = set()  # track which checksums already seen
removed_duplicates = 0  # count duplicates

for name, size, chk in files:  # loop through each file entry
    if chk not in seen_checksums:  # if this checksum hasn't appeared yet
        unique_files.append((name, size, chk))  # keep this file
        seen_checksums.add(chk)  # mark checksum as seen
    else:  # if checksum already seen
        removed_duplicates += 1  # count this as a removed duplicate


total_unique_size = 0 # compute total unique size
for _, size, _ in unique_files:  # loop over unique files
    total_unique_size += size  # sum their sizes

for label, capacity in drives.items():  # go through each drive
    if total_unique_size <= capacity:  # if total fits
        fits_all = True  # mark it fits
        overflow = 0  # no overflow
    else:  # if exceeds capacity
        fits_all = False  # does not fit
        overflow = total_unique_size - capacity  # compute overflow amount


    print(f"{label}: capacity={capacity} MB, fits_all={fits_all}", end="")
    if not fits_all:  # if not fitting
        print(f", overflow={overflow} MB")  # print overflow
    else:  # if it fits
        print()  # just move to next line


print("Kept files:", [f[0] for f in unique_files])
print("Removed duplicates:", removed_duplicates)
print(f"Total unique size: {total_unique_size} MB")


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

