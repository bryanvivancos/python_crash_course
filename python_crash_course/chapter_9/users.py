class User:
    #creating an user class and his attributes
    def __init__(self,first_name,last_name,age,rol):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.rol = rol
    
    #creating two methods for this new class
    def describe_user(self):
        print(f'Current user name is {self.first_name} {self.last_name}, is {self.age} yrs old and his rol in the enterprise is {self.rol}')
    
    def greet_user(self):
        print(f'Hi {self.first_name} {self.last_name}, welcome to our comunity')

#instance 3 times the class
user1 = User('Bryan','Vivanco',26,'System chief')
user2 = User('Sebástian','Vivanco',19,'apprentice')
user3 = User('Ximena','Vivanco',17,'intern')

#calling the methods classes
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()