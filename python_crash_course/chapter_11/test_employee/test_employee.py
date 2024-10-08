from employee import Employee
#test given a raise to an employee
def test_give_default_raise():
    emp = Employee('Bryan','Vivanco',1_500)
    giving_raise = emp.give_raise()
    assert giving_raise == 6_500       
    
def test_give_custom_raise():
    emp = Employee('Bryan','Vivanco',1_500)
    giving_raise = emp.give_raise(7_000)
    assert giving_raise == 8_500   