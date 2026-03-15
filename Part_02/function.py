'''
Part of code that we writen once and used it again 
and again inseted of writing agaian and again,
Perform the same task,
can be used at many places
'''

# WithOut Function
a=21 ; b = 21
print(a + b) # 1st time used

a = 1 ; b = 2 
print(a + b) # 2nd time used

a = 2 ; b = 4
print(a + b) # 3rd time used 

print('\n')
print('With Function')

# With Functions
def add(a , b):
    return a + b 

print(add(21,21))
print(add(1,2))
print(add(2,4))


# Types if Functions
'''
Type 1 — Built-in Functions
These functions are already provided by Python.
You can use them directly without defining them
'''
print("Hello")
len("Python")
max([1,5,3])
sum([1,2,3])


'''
Type 2 — User-defined Functions
These functions are created by the programmer using def.
'''

# Function with No-parameter and No-return 
def greet():
    print('Hello, Python learning')

greet()

# function with Parameter and No-return
def greet(name):
    print('Hello', name)

greet('Ali')

# Function with Paramter and return value
def multiply(a,b):
    return a * b

result = multiply(4,3)
print(result)



'''
Some Time the developer donot know how many input parameter 
user will passed, 
'''

'''
*args in python
allow the function to accept the Multiple parameter 
this convert the the input into the "tuple" 
'''
def add_number(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_number(1,2,3))

'''
2️⃣ **kwargs in Python
Concept
**kwargs allows a function to accept multiple keyword arguments.
Python collects them into a dictionary.
'''

def user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":" ,value)

user_info(name='shakir', age=21) # output in dic


