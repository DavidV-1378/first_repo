# 1)

"""number_1 = int(input("Enter one number: "))
number_2 = int(input("Enter the other number: "))

def odd_numbers(number_1, number_2):
    for number in range(number_1, number_2):
        if number % 2 != 0:
            print(f"{number} is odd")

odd_numbers(number_1, number_2)"""

# 2)

"""number_3 = int(input("Enter one number: "))
number_4 = int(input("Enter the other number: "))


def even_numbers_multiples(number_3, number_4):
    for number in range(number_3, number_4, -1):
        if number % 2 == 0:
            if number % 3 != 0:
                print(f"{number}")

even_numbers_multiples(number_3, number_4)"""

# 3)

number_5 = int(input("Enter one number: "))
number_6 = int(input("Enter the other number: "))

def is_prime(number_2) -> bool:
    count = 0
    is_number_prime = False
    
    for number in range(1, number_2 + 1):
        if number_2 % number != 0:
            count += 1
            if count > 2:
                is_number_prime = False
            elif count == 2:
                is_number_prime = True

    return is_number_prime