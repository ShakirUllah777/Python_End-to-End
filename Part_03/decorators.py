'''
Decorators let you add extra behavior to a function, 
without changing the function's code.
A decorator is a function that takes another function 
as input and returns a new function.
'''


'''
Mostly the decorator is used in the Django buildin function
@login_required
@logout
like these
'''

def my_decorators(func):
    def weaper(name):
        print('Function is starting')
        func(name)

    return weaper


@my_decorators
def greet(name):
    print('Hello', name)

greet("Shakir")

