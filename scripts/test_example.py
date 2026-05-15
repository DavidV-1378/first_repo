from dataclasses import dataclass


"""@dataclass(frozen = True)
class Expense:
    category: str
    amount: float


class Ledger:
    def __init__(self) -> None:
        self._items: list[Expense] = []

    def add(self, item: Expense) -> None:
        self._items.append(item)

    def total_for_category(self, cat: str) -> float:
        total:float = 0.0
        for expense in self._items:
            if expense.category == cat:
                total += expense.amount 
        return total
    

ledger_1 = Ledger()
ledger_1.add(Expense("food", 10))
ledger_1.add(Expense("food", 15))

print(ledger_1.total_for_category("food"))"""


@dataclass(frozen = True)
class ProductCode:
    prefix: str
    number: int

    def __post_init__(self) -> None:
        if not self.prefix.strip:
            raise ValueError("Prefix must not be empty")
        if self.number < 0:
            raise ValueError("Number must not be smaller than zero")
        
@dataclass(frozen = True)
class Expense:
    category: str
    amount: float


def parse_expense(line: str) -> Expense|None:
    parts = [part.strip() for part in line.split(";")]
    if len(parts) != 2:
        return None
    
    category, amount_s = parts
    
    try:
        amount = float(amount_s)
    except ValueError:
        return None
    
    try:
        return Expense(category=category, amount = amount)
    except ValueError:
        return None
    

def test_parse_expence_line_valid() -> None:
    expense = parse_expense("food;10.0")
    assert expense is not None
    assert expense.category == "food"
    assert expense.amount == 10.0
    

@dataclass(frozen = True)
class Tag:
    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
        

def parse_tag(text: str) -> Tag|None:
    cleaned = text.strip()
    if not cleaned:
        return None
    
    try:
        return Tag(cleaned)
    except ValueError:
        return None
    

def test_parse_tag_valid() -> None:
    tag = parse_tag(" python   ")
    assert tag is not None
    assert tag.name == "python"

def test_parse_tag_invalid() -> None:
    tag = parse_tag("       ")
    assert tag is not None