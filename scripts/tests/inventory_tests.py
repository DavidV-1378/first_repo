from models_2 import Inventory, StockItem

def test_stock_item_invalid_sell_raises() -> None:
    item = StockItem("item 1", 10.0, 3)
    try: 
        item.sell(4)
        assert False, "Expected value error"
    except ValueError:
        pass

def test_inventory_missing_lookup_return_none() -> None:
    inventory = Inventory()
    inventory.add(StockItem("item 1", 10.0, 3))
    assert inventory.find_by_name("item 2") is None
    
def test_inventory_duplicate_add_raises() -> None:
    inventroy = Inventory()
    inventroy.add(StockItem("item 1", 10.0, 3))
    try:
        inventroy.add(StockItem("item 1", 10.0, 3))
        assert False, "Expected value error"
    except ValueError:
        pass

def test_inventory_computed_inventory_value_after_actions() -> None:
    inventory = Inventory()
    stock_item_1 = StockItem("item 1", 10.0, 3)
    stock_item_2 = StockItem("item 2", 15.0, 5)

    stock_item_1.sell(2)
    stock_item_2.restock(3)

    inventory.add(stock_item_1)
    inventory.add(stock_item_2)
    assert inventory.count == 2
    assert inventory.total_value == 130.0