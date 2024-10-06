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