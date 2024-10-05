class Restaurant:
    #creacion de clase y atributos
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    #definiendo metodos
    def describe_restaurant(self):
        print(f'El restaurante se llama "{self.name}" y cocina {self.cuisine_type}')
        
    def open_restaurant(self):
        print(f'"{self.name}" restaurant is open')
    
    #metodo que define un numero de servicios
    def set_number_served(self,serving):
        if serving >= self.number_served:
            self.number_served = serving
        else:
            print('You cant rollback the number of servings')
    
    #metodo que incremente el numero de servicios
    def increment_number_served(self,increment):
        if increment >= 0:
            self.number_served += increment
        else:
            print('You cant rollback the number of servings')

restaurant = Restaurant('El encuentro','comida marina')
print(f'Restaurant has served {restaurant.number_served} costumers')

restaurant.number_served = 10
print(f'Restaurant has served {restaurant.number_served} costumers')

restaurant.set_number_served(15)
print(f'Restaurant has served {restaurant.number_served} costumers')

restaurant.increment_number_served(2)
print(f'Restaurant has served {restaurant.number_served} costumers')