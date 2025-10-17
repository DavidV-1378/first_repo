seats = ["_", "X", "_", "_", "X", "_", "_", "_", "X"]

seats.append("_")
seats.extend(["X", "_"])
seats.insert(3, "_")

k = 2

firstk = seats.remove("_")
lastk = seats.pop(k)
seats.sort() #ordered
sorted(seats)
print(max(seats))
print(seats.reverse())

print(" ".join(seats))

seats[0] = "y" #muteability
print("y" not in seats)


print(seats.count("_"))
print(seats)

#---------------------------------------------------

location = 45, 87
latitude, longitude = location
print(location)

#location[1] = 2 illegal

#----------------------------------------------------

unique_seats = set(seats)

unique_seats.add(2)
unique_seats.pop()

unique_seats_lists = list(set(seats))
print(unique_seats_lists)
print("y" in unique_seats)
print(unique_seats)

#----------------------------------------------------

print(len(seats) - len(set(seats)) == 0)

#----------------------------------------------------

mydict = {"names": "voisan", "surnames": "david"}
mydict["surnames"] = "David"
print(mydict)
print(mydict.get("names") is None)
print("names" in mydict)
print(mydict.get("David", "nu avem"))
prizes = {5: "ou", 6: "tricou", 7: "paine", 8: "iaurt", 9: "tort", 10: "pantaloni"}
nota = 3
premiu = prizes.get(nota, "nimic")
print(f"ai castigat un {premiu}")

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b) #True
print(a is b) #True
print(a == c) #False
print(a is c) #True

room = {
tuple(["alex", "david"]): 102, 
tuple(["cristi", "daniel"]): 103
}

print(room)months=["january", "february", "march"]
print(months[0:2])
#tuple
#set
#dict

print(len(months[0:2]))
#print(months[len(months)])
print(months[0])

month = 6
days_in_month = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
print(days_in_month[month - 1:month])