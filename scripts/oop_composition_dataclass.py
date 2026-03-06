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
    
    def add(self, e: Expense) -> None:
        self._items.append(e)

    def total(self) -> float:
        return sum(e.amount for e in self._items)
    


def main() -> None:
    a = Expense("12:04:2008", "cat1", 50.0, "note")
    print(a)
    b = Expense("12:04:2010", "cat1", 100.0, "note")
    print(b.__eq__(a))

    c = Ledger()
    c.add(a)
    c.add(b)
    print(c.total())

if __name__ == "__main__":
    main()