my_pizzas = ["Americana","Pepperoni","Hawaiana","BBQ","AllMeats"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("Cheese")
friend_pizzas.append("Mozzarella")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)
    
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
