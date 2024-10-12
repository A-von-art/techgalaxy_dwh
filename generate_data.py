import json
import random
from datetime import datetime, timedelta

def generate_product():
    categories = ["Смартфоны", "Ноутбуки", "Планшеты", "Умные часы", "Наушники"]
    brands = ["Apple", "Samsung", "Google", "Lenovo", "Sony", "Bose"]

    return {
        "product_id": random.randint(1000, 9999),
        "name": f"{random.choice(brands)} {random.choice(['Pro', 'Ultra', 'Lite', 'Max'])}",
        "category": random.choice(categories),
        "price": round(random.uniform(100, 2000), 2),
        "stock": random.randint(0, 1000)
    }

def generate_order(products):
    order = {
        "order_id": random.randint(10000, 99999),
        "user_id": random.randint(1, 1000),
        "order_date": (datetime.now() - timedelta(days=random.randint(0, 365))).isoformat(),
        "total_amount": 0,
        "items": []
    }
    num_items = random.randint(1, 5)
    for _ in range(num_items):
        product = random.choice(products)
        quantity = random.randint(1, 3)
        item_total = product["price"] * quantity
        order["items"].append({
            "product_id": product["product_id"],
            "quantity": quantity,
            "price": product["price"]
        })
        order["total_amount"] += item_total
    order["total_amount"] = round(order["total_amount"], 2)
    return order

def generate_dataset(num_products, num_orders):
    products = [generate_product() for _ in range(num_products)]
    orders = [generate_order(products) for _ in range(num_orders)]
    return products, orders

products, orders = generate_dataset(1000, 10000)

with open('products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False)

with open('orders.json', 'w', encoding='utf-8') as f:
    json.dump(orders, f, ensure_ascii=False)
