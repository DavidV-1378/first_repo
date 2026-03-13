from typing import Any
from math import isnan
from dataclasses import dataclass


class BankAccount:
    def __init__(self, balance: float, owner: str) -> None:
        if balance < 0.0:
            raise ValueError(f"Initial balance, {balance} cannot be negative")
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount: float) -> None:
        if amount <= 0.0:
            raise ValueError(f"Deposit must be positive")
        self.__balance += amount
    def balance(self) -> float:
        return self.__balance
    #def __repr__(self) -> str:
        #return f"Bank account (owner = {self.owner}, balance = {self.__balance: .2f})"
    

class ToDoItem:
    def __init__(self, title: str) -> None:
        self.title = title
        self.done = False
    def mark_done(self) -> None:
        self.done = True
    def __repr__(self) -> str:
        status = "Done" if self.done else "To Do"
        return f"ToDoItem title: {self.title}, status: {status}"

# Create Class safe counter that has an internal value _value of type int, starting with 0.
# Create method inc and dec, dec raise value error if lower than 0 and method get.

class SafeCounter:
    def __init__(self) -> None:
        self._value: int = 0
    def inc(self) -> None:
        self._value += 1
    def dec(self) -> None:
        if self._value <= 0: 
            raise ValueError("Value cannot be below zero")
        self._value -= 1
    def get(self) -> int:
        return self._value
    def __repr__(self) -> str:
        return f"Current value is: {self._value}."

# You are buliding a small cli(terminal) style expense ledger.
# Each input line is a raw record with format: "YYYY-MM-DD;category=<cat>;amount=<float>;note=<text>"
# Invalid lines may exist: missing fields, amount NaN(not a number), negative ot zero amount, category empty.
# 1. Create Class Expense, with fields: date, category, amount and note. Include validation for amount 0> and for catgory not empty.
# 2. Create Class Ledger that contains a list of Expense, methods: addExpense, total, by_category and largest - top <n> by amount, descending.
# ToDo:
# 3. Create function parse_expense that retuns "None" for invalid lines. Parse returns an Expense object or None. (create parse_expenses.py)
# 4. In main, define raw_lines list with at least 5 lines, 2 invalid.
# Parse, add valid expenses, then print: total spent, total by category, top three expenses. 

class Expense:
    def __init__(self, date: str, category: str, amount: float, note: str) -> None:
        date = date.strip()
        category = category.strip()
        note = note.strip()
        
        if amount <= 0.0:
            raise ValueError("Amount must be larger thatn 0.")
        if not category:
            raise ValueError("Category must not be empty.")
        if not date:
            raise ValueError("Date must not be empty.")
        
        self.date: str = date 
        self.category: str = category
        self.amount: float = amount
        self.note: str = note
    
    def __repr__(self) -> str:
        return f"Expense(date: {self.date}, category: {self.category}, amount: {self.amount: .2f}, note: {self.note})"
    
class Ledger:
    def __init__(self) -> None:
        self._items: list[Expense] = []
    def add_expense(self, expense: Expense) -> None:
        self._items.append(expense)
    def total(self) -> float:
        return sum(expense.amount for expense in self._items)
    def by_category(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for e in self._items:
            totals[e.category] = totals.get(e.category, 0.0) + e.amount
        return totals
    def largest(self, n: int) -> list[Expense]:
        if n <= 0:
            return []
        return sorted(self._items, key = lambda e: e.amount, reverse = True)[:n]
    def items(self) -> list[Expense]:
        return list(self._items) # Return a copy, so callers can't mutate internal list


def parse_expense(line: str):
    try:
        parts: list[str] = line.split(";")
        if len(parts) < 4:
            return None
        
        data_value = parts[0]

        details = {}
        for part in parts[1:]:
            if "=" in parts:
                k, v = part.split("=", 1)
                details[k] = v

        category_value = details.get("category", "")
        note_value = details.get("note", "")

        raw_amount = details.get("amount", "")
        amount_value = float(raw_amount)

        if isnan(amount_value):
            return None
        
        return Expense(data_value, category_value, amount_value, note_value)
    
    except (ValueError):
        return None
    




class A():
   def __init__(self) -> None:
       self.x = 1

@dataclass(frozen = True)
class Book:
    title: str
    pages: int

    def __post_init__(self) -> None:
        if not self.title.strip():
            raise ValueError("Title cannot be empty")
        if self.pages <= 0:
            raise ValueError("Number of pages cannot be negative")
        
class Library:
    def __init__(self) -> None:
        self._books: list[Book] = []
    def total_pages(self) -> int:
        return sum(book.pages for book in self._books)
    def add_book(self, book: Book) -> None:
        self._books.append(book)
    def total_by_first_letters(self) -> dict[str,int]:
        totals: dict[str,int] = {}
        for book in self._books:
            letter = book.title[0].upper()
            totals[letter] = totals.get(letter, 0) + 1
        return totals
    def items(self) -> list[Book]:
        return list(self._books)
    
@dataclass(frozen = True)
class TagEntry:
    name:str 

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Name must not be empty")
        

class TagTracker:
    def __init__(self) -> None:
        self._entries: list[TagEntry] = []
        self._count: dict[str, int] = {}

    def add(self, entry: TagEntry) -> None:
        self._entries.append(entry)
        self._count[entry.name] = self._count.get(entry.name, 0) + 1

    def count_entry(self, tag: str) -> int:
        return self._count.get(tag.strip(), 0)
    


@dataclass(frozen = True)
class OrderItem:
    name: str
    price: float
    qty: int

    def __post_init__(self):
        if not self.name:
            raise ValueError("A name must be inputed")
        if self.price < 0.0:
            raise ValueError("Price must be above zero")
        if self.qty < 0: 
            raise ValueError("Quantity must be above zero")
        
    def cost(self) -> float:
        return self.price * self.qty

class Order:
    def __init__(self, customer_id: str) -> None:
        self._customer_id = customer_id
        self._order_items: list[OrderItem] = []

    @property
    def customer_id(self) -> str:
        return self._customer_id
    
    def add_item(self, item: OrderItem):
        self._order_items.append(item)
    
    @property
    def item_count(self) -> int:
        return len(self._order_items)
    
    @property
    def total_cost(self) -> float:
        return sum(item.cost() for item in self._order_items)
    

