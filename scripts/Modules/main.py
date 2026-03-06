from Utils.math_utils import add
import Utils.math_utils as mu
from Utils.string_utils import shout, whisper
from Utils.string_utils import *
from counter import counts_to
from models import Ledger
from models import parse_expense
import models

result: int = mu.add(1,5)
print(result)

print(add(3,7))

result_1: int = mu.add(2,9)
print(result_1)

print(__name__)

def run_program() -> None:
    print(counts_to(5))
    shouting: str = shout("hello")
    print (shouting)
    print(whisper(shouting))
    result: int = mu.add(1,5)
    print(result)
    print("Program Entry_2")

if __name__ == "__main__":
    raw_lines: list[str] = [
        "2026-02-20;category=Groceries;amount=55.20;note=Weekly groceries",
        "2026-02-21;category=Rent;amount=1200.00;note=Monthly rent",
        "2026-02-22;category=;amount=10.00;note=Invalid: empty category",
        "2026-02-23;category=School;amount=NaN;note=Invalid: NaN amount",
        "2026-02-24;category=Tech;amount=899.99;note=New Monitor",
        "2026-02-25;category=School;amount=6.50;note=New books"
    ]

ledger = Ledger()

for line in raw_lines:
    exp = parse_expense(line)
    if exp is not None:
        ledger.add_expense(exp)

print(f"Total Spent: {ledger.total(): .2f}")

category_summary = ledger.by_category()
for cat, total in category_summary.items():
    print(f" {category}: {total:.2f}")