from models import Order, OrderItem, Discount, NoDiscount, PrecentageDiscount, FixedDiscount

def test_order_subtotal() -> None:
    order = Order()
    order.add(OrderItem("Laptop", 1000.0, 1))
    order.add(OrderItem("Mouse", 50.0, 2))

    assert order.subtotal() == 1100.0


def test_order_total_after_no_discount() -> None:
    order = Order()
    order.add(OrderItem("Laptop", 1000.0, 1))

    no_discount = NoDiscount()
    assert order.total_after(no_discount) == 1000.0


def test_order_total_after_percentage_discount() -> None:
    order = Order()
    order.add(OrderItem("Laptop", 1000.0, 1))   
    
    percent_discount = PrecentageDiscount(10.0) 
    assert order.total_after(percent_discount) == 900.0


def test_order_total_after_fixed_discount_correct_amount() -> None:
    order = Order()
    order.add(OrderItem("Laptop", 1000.0, 1))

    fixed_discount = FixedDiscount(100.0)
    assert order.total_after(fixed_discount) == 850.0


def test_order_total_after_discount_works_with_all_types() -> None:
    order = Order()
    order.add(OrderItem("Keyboard", 100.0, 1))

    assert order.total_after(NoDiscount()) == 100.0
    assert order.total_after(PrecentageDiscount(20.0)) == 80.0
    assert order.total_after(FixedDiscount(15.0)) == 85.0