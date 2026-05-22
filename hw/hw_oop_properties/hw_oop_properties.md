### 1. Rectangle with validated setters

**Requirements (text):**
Create a `Rectangle` class:

- stores width and height
- both must be > 0
- use validated setters
- expose read-only computed properties:
  - `area`
  - `perimeter`

### 2. Employee with validated salary and computed tax

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

### 3  — Inventory item

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

### 4  — Shopping Cart 

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

### 5  — Cloud Storage Account 

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
