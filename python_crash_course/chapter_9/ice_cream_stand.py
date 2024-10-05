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

#creating class that inherits from otra class 
class IceCreamStand(Restaurant): 
    
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ['Banana','Cherry','Grape','Lucuma','Pumpkin','Strawberry']
        
    def display_flavors(self):
        print(f'Hi, we are {self.name} and we have this lists of flavors:')
        for i in self.flavors:
            print(f'- {i}')
            
my_ice_cream = IceCreamStand('Rocotito','Heladería')
my_ice_cream.display_flavors()