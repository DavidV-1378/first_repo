from dataclasses import dataclass
from enum import Enum
from typing import Any

"""1. Create an enum `ExpenseType` with:

- `NEED`
- `WANT`
- `SAVING`"""

class ExpenseType(Enum): 
    NEED = "need"
    WANT = "want"
    SAVING = "saving"


"""2. Create a frozen dataclass `Expense` with:

- `date`
- `category`
- `amount`
- `expense_type`
- `note`"""

"""Validate:

- date non-empty
- category non-empty
- amount > 0"""

"""Add:

- classmethod from_raw that returns Expanse

Raw format:

date;category;amount;type;note"""

@dataclass(frozen = True)
class Expense:
    date: str
    category: str
    amount: int
    expense_type: ExpenseType
    note: str

    def __post_init__(self) -> None:
        if not self.date.strip():
            raise ValueError("Date cannot be empty")
        if not self.category.strip():
            raise ValueError("Category cannot be empty")
        if self.amount < 0:
            raise ValueError("Value cannot be lower or equal to zero")
        
    @classmethod    
    def from_raw(cls, line: str) -> Expense:
        parts = [part.strip() for part in line.split(";")]
        if len(parts) != 5:
            raise ValueError("Parts must be equal to five")
        date, category, amount_s, expense_type_s, note = parts
        try:
            expense_type = ExpenseType(expense_type_s.lower())
        except ValueError:
            raise ValueError("Unknown expense type")
        return cls(
            date = date,
            category = category,
            amount = int(amount_s),
            expense_type = expense_type,
            note = note,
        )
        
"""3. Create frozen dataclasses:

- `CategorySummary` with `category`, `count`, `total`
- `LedgerReport` with `count`, `total`, `summaries`"""

@dataclass(frozen = True)
class CategorySummary:
    category: str
    count: int
    total: float

@dataclass(frozen = True)
class LedgerReport:
    count: int
    total: float
    summaries: list[CategorySummary]

"""4. Create a normal class `Ledger` that:

- stores expenses
- maintains an internal category index
- is iterable
- supports `len(ledger)`
- exposes properties `count` and `total`
- exposes method `category_total(category: str) -> float`
- exposes method `build_report() -> LedgerReport`

Report summaries should be sorted by:
a. total descending
b. category ascending"""

class Ledger:
    def __init__(self) -> None:
        self._expenses = []
        self._by_category: dict[str, list[Expense]] = {}

    @property
    def count(self) -> int:
        return len(self._expenses)
    
    @property
    def total(self) -> float:
        return sum(expense.amount for expense in self._expenses)
    
    def add(self, expense: Expense) -> None:
        self._expenses.append(expense)
        #self.by_category

    def category_total(self, category: str) -> float:
        return sum(expense.amount for expense in self._by_category.get(category, []))
    
    def build_report(self) -> LedgerReport:
        summaries = [CategorySummary(
            category = category, 
            count = len(expenses),
            total = sum(expense.amount for expense in expenses),
            )
            for category, expenses in self._by_category.items()
        ]

        summaries.sort(key = lambda item: (-item.total, item.category))
        return LedgerReport(
            count = self.count,
            total = self.total,
            summaries = summaries,
        )
        
        
    def __iter__(self):
         return iter(self._expenses)
    
    def __len__(self):
        return len(self._expenses)