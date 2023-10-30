def sort_by_price(shopping_list):
    return sorted(shopping_list, key=lambda x: x['price'])
print("\nTask 3.12")
shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]
print(sort_by_price(shopping_list))