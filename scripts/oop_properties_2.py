class User:
    def __init__(self, username: str) -> None:
        self._username = username

    @property
    def username(self) -> str:
        return self._username
    
    @username.setter
    def username(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Username must not be empty.")
        self._username = cleaned

user_1 = User("    username  ")

# user_1.username = "    David Voisan "

print(user_1.username)


# 1. Create a class: "Product" that stores a name, unit price and stock quantity
# Validate fields and use property setters. Expose computed property: inventory value = price * quantity

class Product:
    def __init__(self, name: str, unit_price: float, qty: int) -> None:
        self._name = name
        self._unit_price = unit_price
        self._qty = qty

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str) -> None:
        cleaned = value.strip()
        
        if not cleaned:
            raise ValueError("Name must not be empty.")
        
        self._name = cleaned

    @property
    def unit_price(self) -> float:
        return self._unit_price
    
    @unit_price.setter
    def unit_price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Unit price must not be negative.")
        
        self._unit_price = value

    @property
    def qty(self) -> int:
        return self._qty
    
    @qty.setter
    def qty(self, value: int) -> None:
        if value < 0:
            raise ValueError("Quantity must not be negative.")
        
        self._qty = value

    @property
    def inventory_value(self) -> float:
        return self._qty * self._unit_price
    
product_1 = Product("Laptop", 500.0, 1)

print(product_1.name)
print(product_1.unit_price)
print(product_1.qty)

product_1.name = "PC"
product_1.unit_price = 1000.0
product_1.qty = 2

print(product_1.name)
print(product_1.unit_price)
print(product_1.qty)
print(product_1.inventory_value)


# 1. Build a thermostate class that stores: a target temperatue (between 10.0 - 30.0) and exposes a bolean property "is_high"

class Thermostate:
    def __init__(self, target_temperature: float) -> None:
        self._target_temperature = target_temperature

    @property
    def target_temperature(self) -> float:
        return self._target_temperature
    
    @target_temperature.setter
    def target_temperature(self, value: float) -> None:
        if not (10.0 < self._target_temperature < 30.0):
            raise ValueError("Target temperature must be between 10.0 and 30.0 degrees.")
        
        self._target_temperature = value

    @property
    def is_high(self) -> bool:
        return self._target_temperature >= 25.0
    

thermostate_1 = Thermostate(27.5)

print(thermostate_1.target_temperature)
print(thermostate_1.is_high)

thermostate_1.target_temperature = 22.0

print(thermostate_1.target_temperature)
print(thermostate_1.is_high)