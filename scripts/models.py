from dataclasses import dataclass
from typing import Any

# 1. Create and validate a frozen dataclass OrderItem with name, price and qty.
# 2. Add method cost.
# 3. Create a normal class Order(composition) that stores many OrderItems, can add item, is iterable, exposes properties coun and subtotal.
# 4. Create a base class Discount and subclasses: NoDiscount, PrecentageDiscount and FixedDiscount. Each must implement apply.
# 5. Add to Order method total_after(discount: Discount).
# 6. Write tests for subtotal, each discount type and polymorphys usage.

@dataclass(frozen = True)
class OrderItem:
    name: str
    price: float
    qty: int

    def __post_init__(self):
        cleaned_name = self.name.strip()
        if not cleaned_name:
            raise ValueError("Name cannot be empty")
        if self.price <= 0:
            raise ValueError("Price cannot be equal to or lower than zero")
        if self.qty < 0:
            raise ValueError(" Quantity cannot be less than zero")
        
    def cost(self) -> float:
        return self.price * self.qty
    

class Order:
    def __init__(self) -> None:
        self.order_items: list[OrderItem] = []

    def add(self, item: OrderItem) -> None:
        self.order_items.append(item)

    def __iter__(self):
        return iter(self.order_items)
    
    def subtotal(self) -> float:
        return sum(item.cost() for item in self.order_items)
    
    def total_after(self, discount : Discount) -> float:
        return discount.apply(self.subtotal())


class Discount:
    def apply(self, total: float) -> float:
        return NotImplementedError
    
class NoDiscount(Discount):
    def apply(self, total: float) -> float:
        return total
    
class PrecentageDiscount(Discount):
    def __init__(self, percentage: float) -> None:
        if not 0 <= percentage < 100:
            raise ValueError("Percenatge must be between 1 and 100")
        
        self._precenatge = percentage
    
    def apply(self, total: float) -> float:
        return total * (1 - self._precenatge / 100)


class FixedDiscount(Discount): 
    def __init__(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Amount must be larger than zero")
        
        self._amount = amount

    def apply(self, total: float) -> float:
        return total - self._amount 
        
    
