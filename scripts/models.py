from dataclasses import dataclass
from typing import Any
from enum import Enum
from typing import Protocol

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
        
    
"""1. Create a frozen dataclass `OrderLine` with:

- `order_id`
- `sku`
- `quantity`
- `unit_price`

Validate:

- order_id non-empty
- sku non-empty
- quantity > 0
- unit_price > 0

Add property:

- `line_total`

2. Create a frozen dataclass `ParseIssue` with:

- `line_number`
- `raw_line`
- `reason`

3. Create a normal class `OrderBatch` that:

- stores valid order lines
- maintains internal indexes:
  - quantity by sku
  - revenue by sku
- is iterable
- exposes properties `count`, `total_quantity`, and `total_revenue`
- exposes methods `quantity_for(sku: str)` and `revenue_for(sku: str)`

4. Create an `OrderParser` base class with:

- `parse_line(line: str) -> OrderLine`

Subclasses:

- `PipeOrderParser` for `order_id|sku|quantity|unit_price`
- `CsvOrderParser` for `order_id,sku,quantity,unit_price`

Parser contract:

- return `OrderLine` for valid lines
- raise `ValueError` for invalid lines

5. Create an `InvalidLinePolicy` base class with:

- `handle(issue: ParseIssue, result: ImportResult) -> None`

Subclasses:

- `SkipInvalidLines`
- `CollectInvalidLines`
- `StopOnInvalidLine`

6. Create:

- `ImportResult`, which owns one `OrderBatch` and a list of issues
- function `import_orders -> ImportResult`

7. Write tests for:

- both parser subclasses
- collecting invalid lines
- stopping on the first invalid line
- batch indexes"""


@dataclass(frozen = True)
class
    

"""Build a study tracker where the same log can be evaluated by different progress policies.

1. Create an enum `StudyStatus` with:

- `FOCUSED`
- `DISTRACTED`
- `INCOMPLETE`

2. Create a frozen dataclass `StudySession` with:

- `topic`
- `minutes`
- `tasks_done`
- `status`

Validate:

- topic non-empty
- minutes > 0
- tasks_done >= 0

Add:

- classmethod `from_raw(line: str) -> StudySession`
- property `completed`

Raw format:

topic|minutes|tasks_done|status

3. Create a normal class `StudyLog` that:

- stores sessions
- maintains internal indexes:
  - total minutes by topic
  - completed task count by topic
- is iterable
- supports `len(log)`
- supports `bool(log)`
- exposes properties `total_minutes`, `total_tasks`, `topic_count`
- exposes methods `minutes_for(topic: str)` and `tasks_for(topic: str)`

4. Create a base class `ProgressPolicy` with:

- `score(log: StudyLog) -> float`

Subclasses:

- `DurationProgressPolicy`
- `TaskProgressPolicy`
- `BalancedProgressPolicy`

Rules:

- duration policy: 1 point per 25 minutes
- task policy: 3 points per task
- balanced policy: duration points + task points, but distracted sessions count only half their minutes

5. Write tests for:

- parsing
- bool/len/iteration behavior
- indexes
- all progress policies used polymorphically"""


class StudyStatus(Enum):
    FOCUSED = "focused"
    DISTRACTED = "distracted"
    INCOMPLETE = "incomplete"


@dataclass(frozen = True)
class StudySession:
    topic: str
    minutes: int
    tasks_done: int
    status: StudyStatus

    def __post__init__(self):
        if not self.topic.strip():
            raise ValueError("Topic cannot be empty")
        if self.minutes < 0:
            raise ValueError("Minutes must be more thna zero")
        if self.tasks_done < 0:
            raise ValueError("Number of tasks must be zero or more")
        
    @property
    def completed(self):
        return self.status is not StudyStatus.INCOMPLETE
    
    @classmethod
    def from_raw(cls, line: str) -> StudySession:
        parts = line.split("|") 
        if len(parts) != 4:
            raise ValueError("Parts must be equal to four")
        topic_s, minutes_s, tasks_done_s, status_s = parts
        
        return cls(
            topic = topic_s,
            minutes = int(minutes_s),
            tasks_done = int(tasks_done_s),
            status = StudyStatus(status_s.lower()),
        )
    

class ProgressPolicy(Protocol):
    def score(self, log: StudyLog) -> float:
        ...

class DurationProgressPolicy():
    def score(self, log: StudyLog) -> float:
        return log.total_minutes / 25
    
class TaskProgressPolicy():
    def score(self, log: StudyLog) -> float:
        return log.total_tasks * 3
    
class BalancedProgressPolicy():
    def score(self, log: StudyLog) -> float:
        total_minutes = 0

        for session in log:
            if session.status is StudyStatus.DISTRACTED:
                total_minutes += session.minutes * 0.5
            elif session.status is StudyStatus.FOCUSED:
                total_minutes += session.minutes
            
        return (total_minutes / 25) + (log.total_tasks * 3)
    

def progress_scores(log: StudyLog, policies: list[ProgressPolicy]) -> list[float]:
    return [policy.score(log) for policy in policies]

