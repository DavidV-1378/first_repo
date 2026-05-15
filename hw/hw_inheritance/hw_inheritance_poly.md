# I. **Requirements:**

Build a reporting layer for a ledger. The ledger should not know whether a report is printed as text, CSV, or Markdown.

1. Create an enum `ExpenseType` with:

- `NEED`
- `WANT`
- `SAVING`

1. Create a frozen dataclass `Expense` with:

- `date`
- `category`
- `amount`
- `expense_type`
- `note`

Validate:

- date non-empty
- category non-empty
- amount > 0

Add:

- classmethod from_raw that returns Expanse

Raw format:

date;category;amount;type;note

1. Create frozen dataclasses:

- `CategorySummary` with `category`, `count`, `total`
- `LedgerReport` with `count`, `total`, `summaries`

1. Create a normal class `Ledger` that:

- stores expenses
- maintains an internal category index
- is iterable
- supports `len(ledger)`
- exposes properties `count` and `total`
- exposes method `category_total(category: str) -> float`
- exposes method `build_report() -> LedgerReport`

Report summaries should be sorted by:
a. total descending
b. category ascending

1. Create base class `ReportFormatter` with format method

Subclasses:

- `PlainTextReportFormatter`
- `CsvReportFormatter`
- `MarkdownReportFormatter`

1. Write tests for:

- parsing
- ledger totals and category index
- report sorting
- all formatters used polymorphically

# II. *Requirements :**

Build a study tracker where the same log can be evaluated by different progress policies.

1. Create an enum `StudyStatus` with:

- `FOCUSED`
- `DISTRACTED`
- `INCOMPLETE`

1. Create a frozen dataclass `StudySession` with:

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

1. Create a normal class `StudyLog` that:

- stores sessions
- maintains internal indexes:
  - total minutes by topic
  - completed task count by topic
- is iterable
- supports `len(log)`
- supports `bool(log)`
- exposes properties `total_minutes`, `total_tasks`, `topic_count`
- exposes methods `minutes_for(topic: str)` and `tasks_for(topic: str)`

1. Create a base class `ProgressPolicy` with:

- `score(log: StudyLog) -> float`

Subclasses:

- `DurationProgressPolicy`
- `TaskProgressPolicy`
- `BalancedProgressPolicy`

Rules:

- duration policy: 1 point per 25 minutes
- task policy: 3 points per task
- balanced policy: duration points + task points, but distracted sessions count only half their minutes

1. Write tests for:

- parsing
- bool/len/iteration behavior
- indexes
- all progress policies used polymorphically

# III. **Requirements :**

Build a small inventory and order system. Use composition for products/orders/inventory, and inheritance only for shipping strategies.

1. Create a frozen dataclass `ProductCode` with:

- `value`

Validate:

- non-empty

Add:

- classmethod `from_text(text: str) -> ProductCode` that normalizes to uppercase

1. Create a frozen dataclass `Product` with:

- `code`
- `name`
- `category`
- `price`
- `weight_kg`

Validate:

- name non-empty
- category non-empty
- price > 0
- weight_kg > 0

1. Create a normal class `StockRecord` with:

- `product`
- validated property `quantity`
- property `inventory_value`

1. Create a normal class `Inventory` that:

- stores stock records by `ProductCode`
- maintains an internal category index
- supports `len(inventory)`
- supports `code in inventory`
- exposes properties `total_units` and `total_value`
- exposes `products_in_category(category: str) -> list[Product]`
- has `receive(product: Product, quantity: int) -> None`
- has `fulfill(order: Order) -> None`, reducing stock or raising `ValueError`

1. Create frozen dataclass `OrderItem` with:

- `product`
- `quantity`

1. Create class `Order` that:

- stores order items
- is iterable
- exposes properties `subtotal`, `total_weight`, and `count`

1. Create base class `ShippingPolicy` with:

- `shipping_cost(order: Order) -> float`

Subclasses:

- `PickupShipping`
- `FlatRateShipping`
- `WeightBasedShipping`
- `FreeOverThresholdShipping`

1. Write tests for:

- stock receiving and indexes
- fulfillment reducing stock
- at least three shipping policies used polymorphically

# IV. **Requirements:**

Build an order import pipeline with two separate polymorphic roles:

- parsers decide how to read a line
- invalid-line policies decide what to do when a line is bad

1. Create a frozen dataclass `OrderLine` with:

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

1. Create a frozen dataclass `ParseIssue` with:

- `line_number`
- `raw_line`
- `reason`

1. Create a normal class `OrderBatch` that:

- stores valid order lines
- maintains internal indexes:
  - quantity by sku
  - revenue by sku
- is iterable
- exposes properties `count`, `total_quantity`, and `total_revenue`
- exposes methods `quantity_for(sku: str)` and `revenue_for(sku: str)`

1. Create an `OrderParser` base class with:

- `parse_line(line: str) -> OrderLine`

Subclasses:

- `PipeOrderParser` for `order_id|sku|quantity|unit_price`
- `CsvOrderParser` for `order_id,sku,quantity,unit_price`

Parser contract:

- return `OrderLine` for valid lines
- raise `ValueError` for invalid lines

1. Create an `InvalidLinePolicy` base class with:

- `handle(issue: ParseIssue, result: ImportResult) -> None`

Subclasses:

- `SkipInvalidLines`
- `CollectInvalidLines`
- `StopOnInvalidLine`

1. Create:

- `ImportResult`, which owns one `OrderBatch` and a list of issues
- function `import_orders -> ImportResult`

1. Write tests for:

- both parser subclasses
- collecting invalid lines
- stopping on the first invalid line
- batch indexes

# V. **Requirements:**

Build a gradebook system where different grading rules can be swapped without changing the `StudentRecord` class.

1. Create an enum `Category` with:

- `HOMEWORK`
- `QUIZ`
- `EXAM`

1. Create a frozen dataclass `Assessment` with:

- `student_id`
- `category`
- `name`
- `score`
- `max_score`

Validate:

- student_id non-empty
- name non-empty
- score >= 0
- max_score > 0
- score <= max_score

Add:

- property `percent`
- classmethod `from_raw(line: str) -> Assessment`

Raw format:

student_id;category;name;score;max_score

Example:
S1;quiz;Quiz 1;8;10

1. Create a normal class `StudentRecord` that:

- stores many assessments
- rejects assessments for a different student
- maintains an internal index by category
- is iterable
- supports `len(record)`
- supports `"Quiz 1" in record`
- exposes read-only properties `student_id`, `count`, and `overall_percent`
- exposes method `category_percent(category: Category) -> float`

1. Create a base class `GradingPolicy` with:

- `final_percent(record: StudentRecord) -> float`

1. Create subclasses:

- `OverallPercentPolicy`
- `DropLowestQuizPolicy`
- `WeightedCategoryPolicy`

Rules:

- overall percent uses all points
- drop-lowest quiz removes the lowest quiz only if there are at least two quizzes
- weighted category policy accepts category weights in the constructor

1. Write tests for:

- parsing raw lines
- the internal category index
- `len(...)` and `in`
- at least two grading policies used polymorphically
