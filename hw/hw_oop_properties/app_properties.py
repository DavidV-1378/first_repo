from models_properties import Rectangle, Employee, InventoryItem, ShoppingCart, CartItem

# 1)
rectangle_1 = Rectangle

rectangle_1(5, 10)

# 2)
employee_1 = Employee

employee_1("John Employee", 5000.0)
print(f"Annual salary: {employee_1.annual_salary}")
print(f"Estimated tax: {employee_1.estimated_tax}")

# 3)
item_1 = InventoryItem

item_1("Wireless Mouse", 25.0, 10)
print(f"Item: {item_1.name}")
print(f"Stock: {item_1.stock}")
print(f"Total Value: ${item_1.inventory_value}")

# 4)

cart_1 = ShoppingCart("Cart Owner")

item_1 = CartItem("Laptop", 1000.0, 1)
item_2 = CartItem("Mouse", 20.0, 2)

cart_1.add_item(item_1)
cart_1.add_item(item_2)

print(f"Current Total Price: {cart_1.total_price}")

# 5)

