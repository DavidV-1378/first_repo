a = {"x": 2, "y": 3}
b = {"y": 10, "z": 6}

print(a | b)


elements = {"hydrogen": 
            {"number": 1, "weight": 2, "symbol": "H"},
            "helium": 
            {"number": 2, "weight": 4, "symbol": "He"}
            }
print(elements["hydrogen"]["number"])

oxygen = {"number": 8, "weight": 16, "symbol": "O"}
elements["oxygen"] = oxygen

students = [{"name": "Ionel", "grades": {"maths": 2, "english": 7, "chemestry": 9}},
            {"name": "Georgel", "grades": {"maths": 6, "english": 8, "chemestry": 5}}]

avrages = {}
for student in students:
    grades = student["grades"]
    name = student["name"]
    avrage = sum(grades.values()) / len(grades)
    avrages[name] = avrage
    subjects = set(student["grades"].keys())
    print(student["name"], avrage,)

print(max(avrages.values()), subjects)

#print(elements{"name"},)