# HW OOP Indexes

### HW1 — Bookstore with genre counts

Create a bookstore system:

- Each book has:
  - title
  - genre
  - price
- Validate:
  - title non-empty
  - genre non-empty
  - price positive
- The bookstore stores all books.
- Maintain an internal dictionary:
  - `genre -> count of books`
- Support:
  - adding a book
  - count for a genre
  - total number of books

---

### HW2 — Course roster with group index

Create a course roster:

- Each student has:
  - name
  - group
  - grade
- Validate:
  - name non-empty
  - group non-empty
  - grade between 0 and 10 inclusive
- Maintain:
  - list of all students
  - `group -> list of students`
- Support:
  - add student
  - students in a group
  - average grade in a group, or `None` if group empty

---

### HW3 — Order manager with customer revenue index

Build an order management system:

- Each order item has:
  - name
  - price
  - quantity
- Each order has:
  - customer id
  - many order items
- Validate properly.
- The order manager stores many orders.
- Maintain an internal dictionary:
  - `customer_id -> total revenue`
- Support:
  - add order
  - total revenue
  - revenue for one customer
  - top N customers by revenue

### HW4

Answer in writing:

1. When is recomputing better than maintaining an index?  
2. When is maintaining an index better than recomputing?  
3. Why does deletion make indexed systems more error-prone?