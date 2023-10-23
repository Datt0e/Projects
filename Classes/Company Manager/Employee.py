class Employee:
    
    def __init__(self,lastname,forename,age):
        self.lastname = lastname
        self.forename = forename
        self.age = age

class HourlyEmployee(Employee):
    def __init__(self,lastname,forename,age,weeks,hours,hourly_wage):
        super().__init__(lastname,forename,age)
        self.weeks = weeks
        self.hours = hours
        self.hourly_wage = hourly_wage

#Should this be in the Company class
    def get_pay(self):
        return self.weeks * self.hours * self.hourly_wage

    def set_hourly_wage(self,new_pay):
        self.hourly_wage = new_pay

class SalariedEmployee(Employee):
    def __init__(self,lastname,forename,age,weeks,paycheck,check_durat):
        super().__init__(lastname,forename,age)
        self.weeks = weeks
        self.paycheck = paycheck
        self.check_durat = check_durat

class Manager(Employee):
    pass

class Executive(Employee):
    pass
        

class Company(Employee):
    def fire_emp(employee):
        del employee

    def hire_emp():
        pass

    def raise_emp():
        pass

emp_1 = HourlyEmployee("mama","joe",69,30,40,20)

emp_1.get_pay()

Company.fire_emp(emp_1)

emp_1.get_pay()
