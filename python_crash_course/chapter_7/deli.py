sandwich_orders = ["chicken", "ham", "veggie", "tuna"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

    print(f"I made your {sandwich.title()}")

print("\nThis sandwiches are finished:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")