'''
Classes in python,
In Python, a class is a blueprint for creating objects. It allows you to group data (variables) 
and functions (methods) together in a structured way.
Think of a class as a template, and objects as instances created from that template.

Exmple,
    making the bank form once and then evry new user will come, get the form and then fill the
    form and account will be created, no need to create the form again and again for the new user
    as its once.
    
'''

# Problem - wnat to store the studdent data 
'''
Problems
❌ Code becomes messy with many students
❌ Hard to manage large data
❌ Repeated code
❌ No structure
'''
student1_name = 'Malik'
student1_age = 21
student1_code = 122

student2_name = 'Harry'
student2_age = 12
student2_code = 211

# Solution 
# class Student:
#     def __init__(self, name , age , code):
#         self.name = name
#         self.age = age
#         self.code = code

#     def display(self):
#         print('Name: ',self.name)
#         print('Age: ',self.age)
#         print('code: ',self.code)


# # inheritance 
# class Student_class(Student):
#     def __init__(self, name, age, code, country):
#         super().__init__(name, age, code)
#         self.country = country


# # creating marks 
# student1 = Student('Malik',21,111)
# student2 = Student('Harry', 12, 222)

# # calling the method
# student1.display()
# print('----------')
# student2.display()

# # inheritance 
# s1 = Student_class('hassan',21,121,'pakistan')
# print(s1.display())


class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model
        Car.total_car += 1

    def full_name(self):
        return f"{self.brand} {self.__model}"
    
    def fuel_type(self):
        print('Petrol and Disel')

    # static methods
    @staticmethod
    def car_description():
        return 'Car are menas of Transport.'

    @property
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_type):
        super().__init__(brand, model)
        self.battery_type = battery_type

    def fuel_type(self):
        print('electric battery.')


my_elicar = ElectricCar("Tesla", "Model S", "86kWh")
print(my_elicar.fuel_type())


Safari = Car('Tata', 'Safari')
print(Safari.fuel_type())
print(Car.car_description())
print(Safari.model)

