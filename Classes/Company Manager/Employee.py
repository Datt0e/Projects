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

    def get_pay(self):
        return self.weeks * self.hours * self.hourly_wage


class SalariedEmployee(Employee):
    pass

class Manager(Employee):
    pass

class Executive(Employee):
    pass
        
