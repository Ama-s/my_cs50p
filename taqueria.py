total = 0
while True:
    try:
        order = input("Item: ").title()
        item_available = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
        for each in item_available:
            if order == each:
                price = item_available[each]
                total = total + float(price)
                print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        break
