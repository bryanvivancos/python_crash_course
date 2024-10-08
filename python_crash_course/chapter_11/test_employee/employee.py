class Employee:
    """method that take name and salary of an employee"""
    def __init__(self,first, last,salary):
        self.first_name = first
        self.last_name = last
        self.annual_salary = salary
    
    def give_raise(self,sal_raise = 5000):
        self.annual_salary += sal_raise
        return self.annual_salary