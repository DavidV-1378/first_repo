from dataclasses import dataclass
from typing import Any

@dataclass(frozen = True)
class Expense:
    date: str
    category: str
    amount: int
    note: str

    @classmethod
    def from_line(cls, line: str) -> Expense:
        parts = [p.strip() for p in line.split(";")]

        return cls(date = parts[0], category = parts[1], amount = int(parts[2]), note = parts[3])

line = "2026-03-20 ; grocerise ; 7 ; weekly"

expense_1 = Expense.from_line(line)

print(expense_1)
print(expense_1.amount)


class MathHelper:
    @staticmethod
    def clamp(value: float, low: float, high: float) -> float:
        return max(low, min(high, value))
    
result = MathHelper.clamp(15.0, 0.0, 10.0)
print(result)