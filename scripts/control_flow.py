money = 6
balance = 8

if money < 5:
    balance = 10
elif money == 5:
    balance += 20
else:
    balance = "rich"

print(balance)

answer = 10
guess = 5

if guess == answer:
    print("correct")
elif guess < answer:
    print("Too low")
else:
    print("Too high")

towns = ["barcelona", "bucarest", "madrid" ]

for i in range(len(towns)):
    towns[i] = towns[i].title()

for town in towns:
    town.title()

print(towns, "aici")

capitalised_towns = []
for town in towns: #towns = iterabil
    capitalised_towns.append(town.title())
    print(town)

for i in range(0, 5, 2): #start = 0, stop = 2, step = 1
    print(i)

for i in range(5, 31, 5):
    print(i)