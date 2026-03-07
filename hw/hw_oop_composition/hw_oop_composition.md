# HW OOP Composition

### 1.1 - Extend the library

Extend the library system so it can:

- return the maximum number of pages across all books (or `None` if empty)
- return all book titles sorted alphabetically

---

### 2.1 — Extend the ledger

Extend the ledger so it can:

- return only expenses from a given category
- return only expenses with amount at least a minimum threshold

---

### 2.2 — Import ledger from raw lines (light parsing)

Write code that:

- reads a list of strings formatted as `date;category;amount;note`
- builds a ledger from those lines
- skips invalid lines without crashing

---

### 2.3 — Ledger reports

Extend the ledger so it can:

- compute the average expense per category
- compute the total spending for a month prefix like `YYYY-MM` (by matching the date prefix)

---

### 3.1 - Orders domain system (new domain)

Create an “order processing” system:

- There are orders, and each order contains multiple items.
- Each item has a name, price, and quantity.
- Validate: item name non-empty, price positive, quantity positive.
- Each order belongs to a customer identifier (non-empty).
- Each order can compute its total cost.
- An order manager stores many orders and can compute:
  - total revenue across all orders
  - top N customers by total revenue (descending)

---

### 3.2 — Maintain a revenue index

Improve the order manager so it maintains an internal dictionary:

- maps customer → total_spent
- stays correct whenever a new order is added
- supports returning top customers efficiently
