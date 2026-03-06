# composition = has a relationship

# dataclass = class used to store data (not implement behaviour)
# for a dataclass, python generates: 
# an init method that sets fields, a repr method for debugging, automatic equality for comperison and optional ordering
# frozen = "frozen = True", makes the object immutable after creation
# even though dataclass generates init, we can still validate using "__post_init__" which runs right after the object is created

from dataclasses import dataclass

@dataclass(frozen = True)
class Expense: 
    date: str 
    category: str 
    amount: float
    note: str

    # Validation is done in __post_init__
    def __post_init__(self) -> None:
        if self.amount <= 0.0:
            raise ValueError("Ammount cannot be negative")


class Ledger:
    def __init__(self) -> None:
        self._items: list[Expense] = []
        self._totals_by_catgeory = {}
        self._by_category: dict[str, list[Expense]] = {}
    
    def add(self, e: Expense) -> None:
        self._items.append(e)
        self._totals_by_category[e.category] = (
            self._totals_by_catgeory.get(e.category, 0.0) + e.amount
        )
        if e.category not in self._by_category:
            self._by_category[e.category] = []
        self._by_category[e.category].append(e)

    def expenses_in_category(self, catgeory: str) -> list[Expense]:
        return list(self._by_category.get(catgeory, []))
    
    def total(self) -> float:
        return sum(e.amount for e in self._items)
    
    def total_by_catgeory(self, catgeory: str) -> float:
        return self._totals_by_category.get(catgeory, 0.0)
    


def example() -> None:
    a = Expense("12:04:2008", "cat1", 50.0, "note")
    print(a)
    b = Expense("12:04:2010", "cat1", 100.0, "note")
    print(b.__eq__(a))

    c = Ledger()
    c.add(a)
    c.add(b)
    print(c.total())

def main() -> None:

# internal index dictionary
# category -> total amount
# category -> list of expenses

# simplicity vs speed -> single source of truth vs cached state

# design rules:
# 1. full item list is still base record
# 2. index is derived from items
# 3. maintaining the index incrementally, every mutation method must update both structures
# 4. chose indexing when the query is common, update rules are manageble and performance benefit is worth it
# example:

def by_category(self) -> dict[str,float]:
    totals: {}
    for e in self._items:
        totals[e.category] = totals.get(e.category, 0.0) + e.amount
    
    return totals

    #indexed design:

self._totals_by_category[e.category] = (
    self._totals_by_catgeory.get(e.category, 0.0) + e.amount
)

if __name__ == "__main__":
    main()