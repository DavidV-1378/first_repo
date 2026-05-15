### HW1 (easy) — Rectangle with validated setters

**Requirements (text):**
Create a `Rectangle` class:

- stores width and height
- both must be > 0
- use validated setters
- expose read-only computed properties:
  - `area`
  - `perimeter`

#### Solution

```python
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError("width must be > 0")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError("height must be > 0")
        self._height = value

    @property
    def area(self) -> float:
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
```

---

### HW2 (medium) — Employee with validated salary and computed tax

**Requirements (text):**
Create an `Employee` class:

- stores:
  - name
  - monthly salary
- validate:
  - name non-empty
  - monthly salary > 0
- use setters
- expose read-only properties:
  - `annual_salary`
  - `estimated_tax` equal to 10% of annual salary

#### Solution

```python
class Employee:
    def __init__(self, name: str, monthly_salary: float) -> None:
        self.name = name
        self.monthly_salary = monthly_salary

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("name must be non-empty")
        self._name = cleaned

    @property
    def monthly_salary(self) -> float:
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, value: float) -> None:
        if value <= 0:
            raise ValueError("monthly_salary must be > 0")
        self._monthly_salary = value

    @property
    def annual_salary(self) -> float:
        return self.monthly_salary * 12

    @property
    def estimated_tax(self) -> float:
        return self.annual_salary * 0.10
```

---

### HW3 (hard) — Inventory item: decide setter vs method

**Requirements (text):**
Create an `InventoryItem` class:

- stores:
  - name
  - unit price
  - quantity in stock
- validate fields
- use property setters for:
  - name
  - unit price
- do **not** allow arbitrary direct assignment to stock via a public setter
- instead provide methods:
  - `restock(amount)`
  - `sell(amount)`
- `sell` must fail if not enough stock
- expose read-only properties:
  - `stock`
  - `inventory_value`

#### Solution

```python
class InventoryItem:
    def __init__(self, name: str, unit_price: float, stock: int) -> None:
        self.name = name
        self.unit_price = unit_price
        if stock < 0:
            raise ValueError("stock must be >= 0")
        self._stock = stock

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("name must be non-empty")
        self._name = cleaned

    @property
    def unit_price(self) -> float:
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("unit_price must be > 0")
        self._unit_price = value

    @property
    def stock(self) -> int:
        return self._stock

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("restock amount must be > 0")
        self._stock += amount

    def sell(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("sell amount must be > 0")
        if amount > self._stock:
            raise ValueError("not enough stock")
        self._stock -= amount

    @property
    def inventory_value(self) -> float:
        return self.unit_price * self.stock
```

**Discussion point:**  
This is the most important design example of the lesson:

- price replacement is a setter
- stock changes are domain actions, so methods are better

---

### HW4 (hard) — Shopping Cart (Composition + Setters Integration)

**Requirements (text):**
Create a `CartItem` class:

- stores:
  - `name` (string)
  - `price` (float)
  - `quantity` (int)
- validate fields:
  - `name` must be non-empty (cannot be changed after creation, read-only property)
  - `price` must be > 0 (use validated setter)
  - `quantity` must be >= 0 (use validated setter)
- expose a read-only computed property `subtotal` (`price * quantity`).

Create a `ShoppingCart` class (integrates Week A1/A2 Composition):

- stores:
  - `owner` (string, use validated setter for non-empty)
  - `items` (dictionary mapping item `name` to `CartItem` instance)
- provide a method `add_item(item: CartItem)`:
  - if an item with the same name already exists in the cart, update its quantity by adding the new item's quantity (using the `quantity` setter).
  - otherwise, add it to the dictionary.
- expose a read-only computed property `total_price` which sums the subtotals of all items.

#### Solution

```python
class CartItem:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        cleaned_name = name.strip()
        if not cleaned_name:
            raise ValueError("name must be non-empty")
        self._name = cleaned_name
        self.price = price
        self.quantity = quantity

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("price must be > 0")
        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValueError("quantity must be >= 0")
        self._quantity = value

    @property
    def subtotal(self) -> float:
        return self.price * self.quantity

class ShoppingCart:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._items: dict[str, CartItem] = {}

    @property
    def owner(self) -> str:
        return self._owner

    @owner.setter
    def owner(self, value: str) -> None:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("owner must be non-empty")
        self._owner = cleaned

    def add_item(self, item: CartItem) -> None:
        if item.name in self._items:
            # Reuses the quantity setter for validation
            self._items[item.name].quantity += item.quantity
        else:
            self._items[item.name] = item

    @property
    def total_price(self) -> float:
        return sum(item.subtotal for item in self._items.values())
```

**Discussion point:**  
This problem combines internal dictionary composition (from Week A2) with today's validated setters and computed properties. It also demonstrates how one object (`ShoppingCart`) can manipulate another (`CartItem.quantity`) safely through its setter!

---

### HW5 (hard) — Cloud Storage Account (Properties + Basic Python Control Flow)

**Requirements (text):**
Create a `CloudStorage` class that manages user storage quotas
Takes a `username` and `tier` (string). Initial `used_storage` is 0.0.
- **Fields**:
  - `username`: 
  - `tier`: .
    - Valid tiers are `"free"`, `"pro"`, and `"enterprise"`.
    - When `tier` is set, also update an internal hidden value `_storage_limit` using a **`match`** statement:
      - `"free"` -> 5.0
      - `"pro"` -> 100.0
      - `"enterprise"` -> 1000.0
      - Any other value -> raise `ValueError("Invalid tier")`.
  - `used_storage`: use a validated setter.
    - Must be `>= 0.0`.
    - Cannot exceed the current `storage_limit`. If it does, raise `ValueError()`.
- **Read-only computed properties**:
  - `storage_limit`: exposes the internal storage limit that was set by the tier.
  - `usage_percentage`: computes `(used_storage / storage_limit) * 100.0`.
- **Methods**:
  - `upload_files(file_sizes: list[float])`: Takes a list of file sizes.
    - Use a **`for` loop** to calculate the total size of the files.
    - Add the total size to `used_storage` (this should automatically rely on the setter for validation against the limit).


---

### HW6 (optional stretch) — Design reflection

**Requirements (text):**
Answer in writing:

1. When is a setter a good design choice?  
2. When is a method better than a setter?  
3. Why are computed properties usually read-only?
---
