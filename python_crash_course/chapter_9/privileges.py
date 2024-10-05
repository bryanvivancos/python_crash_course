class User:
    #creating an user class and his attributes
    def __init__(self,first_name,last_name,age,rol):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.rol = rol
        self.login_attempts = 0
    
    #creating two methods for this new class
    def describe_user(self):
        print(f'Current user name is {self.first_name} {self.last_name}, is {self.age} yrs old and his rol in the enterprise is {self.rol}')
    
    def greet_user(self):
        print(f'Hi {self.first_name} {self.last_name}, welcome to our comunity')
        
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        
#Separando la clase privilegios de un usuario admin para que no sea tan largo el método
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
        


my_user = Admin('Bryan','Vivanco', 26,'System Chief')
my_user.privileges.show_privileges()