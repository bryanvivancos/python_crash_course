from user_module import User

#modulo que incluye clases de admin

class Privileges:
    
    def __init__(self,privileges = ['can add post','can delete post','can modify post','can change others passwords']):
        self.privileges = privileges
    
        
    def show_privileges(self):
        print(f'Hi, here we are a list of things you can do: ')
        for i in self.privileges:
            print(f'- {i}')
        
class Admin(User):
    
    def __init__(self, first_name, last_name, age, rol):
        super().__init__(first_name, last_name, age, rol)
        #llamando a la clase privilegios como un atributo de la clase admin
        self.privileges = Privileges()