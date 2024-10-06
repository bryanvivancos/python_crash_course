class Restaurant:
    #creacion de clase y atributos
    def __init__(self,name,cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    #definiendo metodos
    def describe_restaurant(self):
        print(f'El restaurante se llama "{self.name}" y cocina {self.cuisine_type}')
        
    def open_restaurant(self):
        print(f'"{self.name}" restaurant is open')

# #instanciando clase
# rest = Restaurant('El encuentro','comida marina')
# #imprimiendo atributos
# print(rest.name)
# print(rest.cuisine_type)
# #llamando ambos métodos
# rest.describe_restaurant()
# rest.open_restaurant()
