text = ("hello world")

def MyFunction(text):
    text = text.strip().title()
    result =  "".join(text.split())
    return result

text = MyFunction(text)

print(text)


def apply_tax(price:int, tax_rate:float)->float: 
    """
    aplies tax to a price
    parameters: price(int) 
    tax rate(float)
    retruns tax price (float)
    raises: "" """
    return price * (1 + tax_rate)

price = apply_tax(17.5, 0.19)
print(price)

counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)


def outer():
    x = 10
    def inner():
        nonlocal x 
        x += 1
    inner()
    return x

result = outer()
print(result)

#lambda functions
products = [("laptop", 1000), ("mouse", 100)]
sorted_products = sorted(products, key = lambda product: product [1])

print(sorted(products), sorted_products)

emails = [ None, "david.voisan@gmail.com", "voisan.david", ""]
#clean_emials = list(filter(lambda email: "@" in email and "." in email, emails))

#print(clean_emials)


evens = list(filter(lambda x: x %2 == 0, range(0, 10)))
print(evens)

result = list(filter(None, emails))
print(result)