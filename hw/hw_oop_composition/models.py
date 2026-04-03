from dataclasses import dataclass

### HW 1.1: ---------------------------------------------------------

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_max_pages(self):
        if not self.books:
            return None
        return max(book.pages for book in self.books)

    def get_sorted_titles(self):
        return sorted(book.title for book in self.books)

### -----------------------------------------------------------------

### -----------------------------------------------------------------

@dataclass(frozen=True)
class Expense: 
    date: str 
    category: str 
    amount: float
    note: str

    def __post_init__(self) -> None:
        if self.amount <= 0.0:
            raise ValueError("Amount cannot be negative or zero")

class Ledger:
    def __init__(self) -> None:
        self._items: list[Expense] = []
        self._totals_by_category: dict[str, float] = {}
        self._by_category: dict[str, list[Expense]] = {}
    
    def add(self, e: Expense) -> None:
        self._items.append(e)
        self._totals_by_category[e.category] = (
            self._totals_by_category.get(e.category, 0.0) + e.amount
        )
        if e.category not in self._by_category:
            self._by_category[e.category] = []
        self._by_category[e.category].append(e)

    def expenses_in_category(self, category: str) -> list[Expense]:
        return list(self._by_category.get(category, []))
    
    def total(self) -> float:
        return sum(e.amount for e in self._items)
    
    def total_by_category(self, category: str) -> float:
        return self._totals_by_category.get(category, 0.0)
    
    ### HW 2.1: ---------------------------------------------------------

    def get_by_category(self, category: str) -> list[Expense]:
        return self._by_category.get(category, [])
    
    def get_above_threshold(self, thereshold: float) -> list[Expense]:
        return [e for e in self._items if e.amount >= thereshold]
    
    ### -----------------------------------------------------------------

    ### HW 2.2: ---------------------------------------------------------

    def ledger_from_strings(self, lines: list[str]) -> Ledger:
        ledger = Ledger()

        for line in lines:
            if not line.strip():
                continue

            try:
                parts = line.strip().strip(';')

                if len(parts) != 4:
                    continue

                data_val, cat_val, amt_str, note_val = parts

                expense = Expense(
                    date = data_val,
                    category = cat_val,
                    amount = float(amt_str),
                    note = note_val
                )

                ledger.add(expense)

            except (ValueError):
                continue

        return ledger
    
    ### -----------------------------------------------------------------
    
    ### HW 2.3: ---------------------------------------------------------

    def average_by_category(self, category: str) -> float:
        expenses = self._by_category.get(category, [])
        if not expenses:
            return 0.0
        
        return self._totals_by_category[category] / len(expenses)
    

    def total_month(self, month_prefix: str) -> float:
        return sum(
            e.amount for e in self._items
            if e.date.startswith(month_prefix)
        )
    
    ### -----------------------------------------------------------------

### HW 3.1 + 3.2: ---------------------------------------------------------
    
@dataclass(frozen=True)
class Item:
    name: str
    price: float
    quantity: int

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Item name must not be empty")
        if self.price <= 0:
            raise ValueError("Price must be positive")
        if self.quantity <= 0:
            raise ValueError("Quantity must be positive")
        
@dataclass
class Order:
    customer_id: str
    items: list[Item] = []

    def __post_init__(self) -> None:
        if not self.customer_id.strip():
            raise ValueError("Customer identifier cannot be empty")
        
        if self.items is None:
            self.items = []

    def total_cost(self) -> float:
        return sum(item.price * item.quantity for item in self.items)
    

class OrderManager:
    def __init__(self) -> None:
        self.orders: list[Order] = []
        ### HW 3.2:
        self.revenue_index: dict[str, float] = {} 
        ### -------

    def add_order(self, order: Order) -> None:
        self.orders.append(order)
        ### HW 3.2:
        cost = order.total_cost()
        id = order.customer_id
        if id in self.revenue_index:
            self.revenue_index[id] += cost
        else:
            self.revenue_index[id] = cost
        ### -------


    def total_revenue(self) -> float:
        return sum(order.total_cost() for order in self.orders)

    def top_customers(self, n: int) -> list[tuple[str, float]]:
        """revenue_map = {}
        
            for order in self.orders:
                id = order.customer_id
                cost = order.total_cost()
            
                revenue_map[id] = revenue_map.get(id, 0.0) + cost"""

        ### HW 3.2:  
        sorted_customers = sorted(
            self.revenue_index.items(), 
            key = lambda item: item[1], 
            reverse = True
        )
        ### -------
        
        return sorted_customers[:n]
        
    ### -----------------------------------------------------------------

