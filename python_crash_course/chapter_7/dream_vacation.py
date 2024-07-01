vacations = {}

polling_active = True

while polling_active:
    name = input("\nWhats your name? ")
    vacation = input("\nIf you could visit one place in the world, where would you go? ")

    vacations[name] = vacation

    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        polling_active = False 

print("\n--- Poll Results ---")

for name, vacation in vacations.items():
    print(f"{name.title()} want to go to {vacation.title()}")