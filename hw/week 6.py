num = [3, 5, 7, 9]

"""total = 0

for n in num:
    total += n

 print(total)

count = 0
while len(num) > count:
    total += num[count]
    count += 1
else:
    print(total)

age = input("Enter age")

while not age.isdigit():
    age = input("Enter a number")
else:
    print(age) 

password = "password123"
password_entered = input("Enter a password")
count = 0

while password != password_entered and count < 3:
    password_entered = input("Enter another password")
    count += 1
    if password == password_entered:
        print("Acces granted")
    else:
        print("Too many attmepts")


import random

number = random.randint(1, 10)
number_guessed = 0
attempts = 0

while number != number_guessed:
    number_guessed = int(input("Enter a number"))
    attempts +=1
    if number_guessed < number:
        print("Number was too small")
    elif number_guessed > number:
        print("Number was too big")
print(f"Number guessed in {attempts}") 

names = ["david", "bogdan", "samuel"]
grades = [8, 6]

for name, grade in zip(names, grades):
    print(f"name:{name} score:{grade}")

for i, name in enumerate(names, start = 1):
    print(i, name)

names = ["david", "bogdan", "samuel"]
grades = [8, 6, 9]



print() """

names = ["david v", "bogdan q", "samuel c"]
capitalized_names = [name.title() for name in names if name == "david"]

"""for name in names:
    capitalized_names.append(name.title())"""

print(capitalized_names)

squared_numbers = [x ** 2 if x % 2 == 0 else x + 5 for x in range(9)]
print(squared_numbers)

first_names = [name.split()[0].title() for name in names]

print(first_names)

grades = [8, 6, 9]

gardes_higher_than_seven = [(name, grade) for name, grade in zip(names, grades) if grade > 7]

print(gardes_higher_than_seven)