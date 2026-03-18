'''
Paradigms,
differnat wat to write python programme(code)
ways are:
    Procedural Programming
    OOPs
    function based code

without this:
    no strcuture and pattern
    code become messay
    hard to handle the large project
'''


# Procedural Programming
# code is writen from top to botem
def add(a,b):
    return a + b

num = add(2,2)
print(num)

# Object Orientaded Programming
# Organized using classes and object
class Car:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

name_car = Car('Tesla')
name_car.show()


# Functional Programming
# use function as 1st class object

numbers = [1,2,3,4,5,6,7,8,9,10]
squre =list(map(lambda x: x**2, numbers))
print(squre)
