sandwich_orders = ["chicken", "pastrami", "ham", "pastrami", "veggie", "tuna", "pastrami"]
finished_sandwiches = []

print(sandwich_orders)
print("Deli has run out of pastrami\n")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

    print(f"I made your {sandwich.title()}")

print("\nThis sandwiches are finished:")

for sandwich in finished_sandwiches:
    print(f"\t{sandwich.title()}")