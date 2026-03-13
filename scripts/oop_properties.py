# How:
# Internal mutable state ussualy lives in "private by convention" attributes such as: _items, _balance
# A property exposes waht outisde code should be allowed to see.
# If outisde code should not assign freely, do not expose raw, writable public attributes.
# Use properties when the information is conceptually part of the object public interface.
# We use @property to define a method as an attribute.

class BankAccount:
    def __init__(self) -> None:
        self._balance = 0.0

    @property
    def balance(self) -> float:
        return self._balance
    

bank_account_1 = BankAccount()

print(bank_account_1.balance)

class Library:
    def __init__(self) -> None:
        self._titles: list[str] = []

    def add_title(self, title: str) -> None:
        self._titles.append(title)

    @property
    def book_count(self) -> int:
        return len(self._titles)
    

library_1 = Library()

library_1.add_title("book1")
library_1.add_title("book2")

print(library_1.book_count)

class Ledger:
    def __init__(self) -> None:
        self._items: list[float] = []
        self._total: float = 0.0

    def add(self, item: float) -> None:
        self._items.append(item)
        self._total += item

    @property
    def total(self) -> float:
        return self._total
    

ledger_1 = Ledger()

ledger_1.add(10)
ledger_1.add(5)

print(ledger_1.total)

class Student:
    def __init__(self, grades: list[float]) -> None:
        self._grades = list(grades)

    @property
    def average(self) -> float:
        return sum(self._grades) / len(self._grades)
    
    @property
    def is_passing(self) -> bool:
        return self.average >= 5
    

student_1 = Student([7, 9, 6, 10, 8])

print(f"David is passing? {student_1.is_passing}")