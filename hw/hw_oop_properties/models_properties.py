# 1)

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        if height <= 0:
            raise ValueError("Height ust be greater than zero")
        if width <= 0:
            raise ValueError("Width must be greater than zero")
        
        self._width = width
        self._height = height
        
    @property
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height
    
    @property
    def area(self) -> float:
        return self._width * self._height

    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height)
    
# 2)

class Employee:
    def __init__(self, name: str, monthly_salary: float) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if monthly_salary <= 0:
            raise ValueError("Monthly salary must be greater than zero")
        
        self._name = name
        self._monthly_salary = monthly_salary

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def monthly_salary(self) -> float:
        return self._monthly_salary
    
    @property
    def annual_salary(self) -> float:
        return self._monthly_salary * 12
    
    @property 
    def estimated_tax(self) -> float:
        return self.annual_salary * 0.10
    

# 3)

class InventoryItem:
    def __init__(self, name: str, unit_price: float, quantity_in_stock: int) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty")
            
        if unit_price < 0:
            raise ValueError("Unit price cannot be below zero")
            
        if quantity_in_stock < 0:
            raise ValueError("Initial stock cannot be below zero")
        
        self._name = name
        self._unit_price = unit_price
        self._stock = quantity_in_stock

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Unit price cannot be below zero")
        self._unit_price = value

    @property
    def stock(self) -> int:
        return self._stock

    @property
    def inventory_value(self) -> float:
        return self._stock * self._unit_price

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Restock amount must be greater than zero")
        self._stock += amount

    def sell(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Sell amount must be greater than zero")
        if amount > self._stock:
            raise ValueError("Not enough stock available for the sale")
        self._stock -= amount

# 4)

class CartItem:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        if quantity < 0:
            raise ValueError("Quantity cannot be below zero")

        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Price must be greater than zero")
        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("Quantity cannot be below zero")
        self._quantity = value

    @property
    def subtotal(self) -> float:
        return self._price * self._quantity


class ShoppingCart:
    def __init__(self, owner: str) -> None:
        if not owner or not owner.strip():
            raise ValueError("Owner name cannot be empty")
        self._owner = owner
        self.items: dict[str, CartItem] = {}

    @property
    def owner(self) -> str:
        return self._owner

    @owner.setter
    def owner(self, value: str) -> None:
        if not value or not value.strip():
            raise ValueError("Owner name cannot be empty")
        self._owner = value

    def add_item(self, item: CartItem) -> None:
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    @property
    def total_price(self) -> float:
        return sum(cart_item.subtotal for cart_item in self.items.values())
    
# 5) 

class CloudStorage:
    def __init__(self, username: str, tier: str):
        if not username:
            raise ValueError("Username cannot be empty")
        self.username = username
        self._used_storage = 0.0
        self.tier = tier

    @property
    def tier(self) -> str:
        return self._tier

    @tier.setter
    def tier(self, value: str):
        match value.lower():
            case "free":
                self._storage_limit = 5.0
            case "pro":
                self._storage_limit = 100.0
            case "enterprise":
                self._storage_limit = 1000.0
            case _:
                raise ValueError("Invalid tier")
        self._tier = value.lower()

    @property
    def used_storage(self) -> float:
        return self._used_storage

    @used_storage.setter
    def used_storage(self, value: float):
        self._used_storage = value

    @property
    def storage_limit(self) -> float:
        return self._storage_limit

    @property
    def usage_percentage(self) -> float:
        if self.storage_limit == 0.0:
            return 0.0
        return (self.used_storage / self.storage_limit) * 100.0

    def upload_files(self, file_sizes: list[float]):
        total_size = 0.0
        for size in file_sizes:
            if size < 0.0:
                raise ValueError("File size cannot be negative.")
            total_size += size
            
        if self.used_storage + total_size > self.storage_limit:
            raise ValueError("Storage limit exceeded.")
            
        self.used_storage += total_size