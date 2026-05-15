from enum import Enum
from dataclasses import dataclass

# Build an expense system, where categories are a Enum(food, transport, books, fun, other)
# Expense stores date, category, amount and note.
# Ledger stores many Expenses and supports len, Expense in ledger and if Ledger, method by_category that retuns dict[category, float]

class Category(Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    BOOKS = "books"
    FUN = "fun"
    OTHER = "other"

@dataclass(frozen = True)
class Expense:
    date: str
    category: Category
    amount: float
    note: str

    def __post_init__(self) -> None:
        if not self.date.strip():
            raise ValueError("Date must not be empty.")
        if self.amount <= 0: 
            raise ValueError("Amounr cannot be zero or negative.")
        
class Ledger:
    def __init__(self) -> None:
        self._expenses: list[Expense] = []

    def add(self, expense: Expense) -> None:
        self._expenses.append(expense)

    def __len__(self) -> int:
        return len(self._expenses) 
    
    def __contains__(self, expense: Expense) -> bool:
        return expense in self._expenses
    
    def __bool__(self) -> bool:
        return len(self._expenses) > 0 
    
    def by_category(self) -> dict[Category, float]: 
        total: dict[Category, float] = {}
        for expense in self._expenses:
            total[expense.category] = total.get(expense.category, 0.0) + expense.amount
        return total
    
# Build a quizz system with a difficulty Enum(easy = 1, medium  = 2, hard = 3)
# Question class stores prompt, answer and difficulty properties and implements custom equlity, comparing by prompt text
# QuestionBank class stores many questions and supports len, question in bank, bank empty, filter by a difficulty -> list[Question]

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


class Question():
    def __init__(self, prompt: str, answer: str, difficulty: Difficulty) -> None:
        cleaned_prompt = prompt.strip()
        if not cleaned_prompt:
            raise ValueError("Promopt must not be empty")
        
        cleaned_asnwer = answer.strip()
        if not cleaned_asnwer:
            raise ValueError("Answer must be given")
        
        self._prompt = cleaned_prompt
        self._answer = cleaned_asnwer
        self._difficulty = difficulty

    def __eq__(self, q2: object) -> bool:
        if not isinstance(q2, Question):
            return NotImplemented
        return self._prompt == q2._prompt
    
    @property
    def prompt(self) -> str:
        return self._prompt
    
    @property
    def answer(self) -> str:
        return self._answer
    
    @property
    def difficulty(self) -> Difficulty:
        return self._difficulty
    
    def __repr__(self) -> str:
        return f"Question(prompt={self._prompt},answer={self._answer}, difficulty={self._difficulty.name})"
    

class QuestionBank():
    def __init__(self) -> None:
        self._questions: list[Question] = []

    def fliter_by_difficulty(self, difficulty: Difficulty) -> list[Question]:
        return [q for q in self._questions if q.difficulty == difficulty]
    
    def add(self, q: Question) -> None:
        self._questions.append(q)
        

# Build a order system with full dunder support and enum: 
# OrderStatus enum: PENDING, CONFIRMED, SHIPPED, DELIVERED and CANCELLED 
# OrderItem class: name, price, qty, custom equal byname.
# Order class: customer, status, items, that supports: len(order), check by OrderItem equality, if order: 
# Truthy when has items, eq: two orders are equal if same customer and same items
# Properties: total cost, status
# Method advance_status that moves to the next status (cannont go past delivered)
# repr and str for both classes

class OrderStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    SHIPPED = 3
    DELIVERED = 4
    CANCELLED = 5


class OrderItem:
    def __init__(self, name: str, price: float, qty: int) -> None:
        cleaned_name = name.strip()
        if not cleaned_name:
            raise ValueError("Name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be 0 or lower.")
        if qty <= 0:
            raise ValueError("Quantity cannot be 0 or lower.")
        
        self._name = cleaned_name
        self._price = price
        self._qty = qty

    @property
    def name(self):
        return self._name 
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, OrderItem):
            return NotImplemented
        return self._name == value._name
    
    def __repr__(self) -> str:
        return f"OrderItem(name={self._name},price={self._price}, qty={self._qty})"
    
    def cost(self) ->  float:
        return self._price * self._qty


class Order:
    _STATUS_FLOW = [OrderStatus.PENDING, OrderStatus.CONFIRMED, OrderStatus.SHIPPED, OrderStatus.DELIVERED]
    
    def __init__(self, customer: str) -> None:
        if not customer.strip():
            raise ValueError("Customer's anme cannot be empty.")
        
        self._customer = customer 
        self._items = []
        self._status = OrderStatus.PENDING

    def add_item(self, item: OrderItem) -> None:
        self._items.append(item)

    @property
    def total_cost(self) -> float:
        return sum(item.cost() for item in self._items)
    
    def advance_status(self) -> None:
        if self._status == OrderStatus.CANCELLED:
            raise ValueError("Can't advance a cancelled order")
        try:
            id = self._STATUS_FLOW.index(self._status)
        except ValueError:
            raise ValueError("Cannot advance from current status")
        if id >= len(self._STATUS_FLOW) - 1:
            raise ValueError("ORder already delivered")
        self._status = self._STATUS_FLOW[id + 1]
        
# 1) Build an inventory module:
# a) a class StockItem with validated property setter for name, unit price, 
# read only property stock, read only computed property value, methods: restock and sell.'
# Cannot sell more than available stock.
# b) A class Inventory that stores StockItems by name, exposes property count, methods: add, find by name.
# Contract: invalid item state or invalid actions raise
# Finding a missing item returns None
# Adding duplicate itme name raises
# Write tests for: missing lookup return None, invalid sell rasing, duplicate add rasing, computed inventory value after restock/sell.

class StockItem:
    def __init__(self, name: str, unit_price: float, stock: int) -> None:
        if not name.strip():
            raise ValueError("Name cannot be empty")
        
        if unit_price <= 0:
            raise ValueError("Unit price cannot be equal or lower than zero.")

        if stock < 0:
            raise ValueError("Stock cannot be lower than zero.")

        self._name = name.strip()
        self._unit_price = unit_price
        self._stock = stock

    @property
    def name(self) -> str:
        return self._name 
    
    @name.setter
    def name(self, value: str) -> None:
        cleaned_name = value.strip()
        if not cleaned_name:
            raise ValueError("Name cannot be empty")
        self._name = cleaned_name 

    @property
    def unit_price(self) -> float:
        return self._unit_price
    
    @unit_price.setter
    def unit_price(self, value: float):
        if value <= 0:
            raise ValueError("Unit price cannot be equal to or lower than zero")
        self._unit_price = value 

    @property
    def stock(self) -> int:
        return self._stock
    
    @property
    def value(self) -> float:
        return self._stock * self._unit_price
    

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount restocked must be greater > 0")
        self._stock += amount 


    def sell(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Amount sold must be greater > 0")
        if amount > self._stock:
            raise ValueError("Not enough stock to sell")
        self._stock -= amount 



class Inventory:
    def __init__(self) -> None:
        self._items: dict[str, StockItem] = {}

    @property
    def count(self) -> int:
        return len(self._items)
    
    @property
    def total_value(self) -> float:
        return sum(stock_item.value for stock_item in self._items.values())

    def add(self, stock_item: StockItem) -> None:
        if not stock_item:
            raise ValueError("An item must be added")
        if stock_item.name in self._items:
            raise ValueError("Duplicate item not allowed")
        self._items[stock_item.name] = stock_item

    def find_by_name(self, name: str) -> StockItem|None:
        return self._items.get(name.strip())

# Run with pytest path 
# Move tests to test file


    
