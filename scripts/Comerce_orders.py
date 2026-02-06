# 1) You are building a mini back office tool for an online job. Create:
# - A catalogue mapping product id to unit price (At least 6 items)
# - raw orders - a list with keys order id, product id, qty and coupon.
# Include: invalid quntity, qty <= 0, unknown product id, coupon empty and missing, 3 valid orders.
# Define parse order that raises custom exceptions: OrderError, ValidationError and PricingError.
# Validate: required keys present, qty int and > 0, coupon optional.
# Return cleaned order dict.
# 2) Define compute total that calculates price with coupon rules:
# - If product id not in catalogue, raise PricingError
# - subtotal = qty * unit price
# Coupons: "NONE" or None - No discount; "SAVE10" - 10% off subtotal, "HALF" - 50% off if subtotal > 100, any other coupon raise ValidationError
# 3) Define apply refund to proccess refund with **kwargs only. Validate precent in 0-100. Return rounded refund amount.
# 4) Proccess all raw orders, valid ones -> proccessed lists; Invlaid ones -> rejected lists. Then produce:
# - Total revenue, revenue per product, top 3 orders by total and a list of all coupons used.
# 5) Create a decorator admin_action(tag: str) returning a decorator that:
# - Prints "[<tag>] calling <func>" and stores an audit record in a list; Works with any signiture; Uses a closure for tag.
# - Decorate compute_total and apply_refund.
# 6) Write 2 asserts for succesful orders, 2 asserts that confirm exceptions are raised.

catalogue: dict[str, float] = {
    "pen": 4.99,
    "notebook": 7.99,
    "pencilcase": 6.99,
    "laptop": 119.99,
    "headset": 34.99,
    "textbook": 14.99
    }
""" raw_orders: list[dict[str, str]] = [
    {"order_id": "001", "product_id": "pen", "qty": "5", "coupon": "NONE"},
    {"order_id": "002", "product_id": "notebook", "qty": "2", "coupon": "SAVE10"},
    {"order_id": "003", "product_id": "laptop", "qty": "1"},
    {"order_id": "004", "product_id": "pencilcase", "qty": "0", "coupon": "SAVE20"},
    {"order_id": "005", "product_id": "unknown", "qty": "3", "coupon": "HALF"},
    {"order_id": "006", "product_id": "textbook", "qty": "-1", "coupon": "SAVE10"},
    {"order_id": "007", "product_id": "headset", "qty": "2", "coupon": " "},
    {"order_id": "008", "product_id": "pen", "qty": "x", "coupon": "NONE"}
] """

raw_orders: list[dict[str, str]] = [
    {"order_id": "001", "product_id": "pen", "qty": "5", "coupon": "NONE"},
    {"order_id": "002", "product_id": "notebook", "qty": "2", "coupon": "SAVE10"},
    {"order_id": "003", "product_id": "laptop", "qty": "1", "coupon": "HALF"}
]

class OrderError(Exception): 
    pass

class ValidationError(OrderError):
    pass

class PricingError(OrderError):
    pass

def admin_action(tag: str):
    log: list[str] = []
    def decorator(func):
        def wrapper(*args, **kwargs):
            message = f"<{tag}> calling function:{func.__name__}"
            log.append(message)
            print(log)
            wrapper.log = log
            result = func(*args, **kwargs)
            return result
        wrapper.log = log
        print(wrapper.log)
        return wrapper
    return decorator 

def parse_order(raw: dict[str, str]) -> dict[str, object]:
    required_keys = ("order_id", "product_id", "qty")
    
    for key in required_keys:
        if key not in raw:
            raise ValidationError(f"Missing required key: {key}")

    order_id = raw["order_id"].strip()
    product_id = raw["product_id"].strip()

    if not order_id:
        raise ValidationError(f"Order id cannot be empty")
    
    if not product_id:
        raise ValidationError(f"Product id cannot be empty")

    try:
        quantity = int(raw["qty"])
    except ValueError as e:
        raise ValidationError(f"Invalid qty: {raw["qty"]}") from e
    
    if quantity <= 0:
        raise ValidationError(f"Quantity must be greater than 0, got {quantity}")
    
    raw_coupon = raw.get("coupon")
    coupon: str | None

    if raw_coupon is None:
        coupon = None
    else:
        c = raw_coupon.strip().upper()
        coupon = c if c else None

    return {"order_id": order_id, "product_id": product_id, "qty": quantity, "coupon": coupon}

parsed_orders = []

for order in raw_orders:
    parsed_orders.append(parse_order(order))

@admin_action("pricing")
def compute_total(cat: dict[str, float], order: dict[str, object]) -> float:
    product_id = str(order["product_id"])
    qty = int(order["qty"])
    coupon = order.get("coupon")
    unite_price = float(cat[product_id])

    if product_id not in cat:
        raise PricingError(f"Unknown product id {product_id}")
    
    coupon_str = None if coupon is None else str(coupon)
    
    subtotal = (qty * unite_price)
    
    if coupon_str is None or coupon_str == "NONE":
        total = subtotal
    elif coupon_str == "SAVE10":
        total = subtotal * 0.9
    elif coupon_str == "HALF":
        if subtotal > 100:
            total = subtotal * 0.5
        else:
            total = subtotal
    else:
        raise ValidationError(f"Coupon is unknown: {coupon_str}")
    
    return round(total, 2)

processed_orders = []
rejected_orders = []

for raw in raw_orders:
    try:
        clean = parse_order(raw)
        total = compute_total(catalogue, clean)
        clean["total"] = total
        processed_orders.append(clean)
    except OrderError as e:
        rejected_orders.append({"raw": raw, "error": str(e)})

total_revenue = sum(o["total"] for o in processed_orders)
revenue_per_product = {}
for o in processed_orders:
    pid = o["product_id"]
    revenue_per_product[pid] = revenue_per_product.get(pid, 0) + o["total"]

top_3 = sorted(processed_orders, key=lambda x: x["total"], reverse=True)[:3]
coupons_used = [o["coupon"] for o in processed_orders if o["coupon"] not in (None, "NONE")]

assert processed[0]["total"] == 24.95 
assert processed[1]["total"] == 14.38