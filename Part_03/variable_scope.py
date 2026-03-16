'''
Variable Scope:
    A variable is only available from inside the region it is created. This is called scope.
Conation 2 type of scope

Local Scope
    variable inside the function
    just can access inside function not outside
Gloabl scope:
    variable outside the function,
    can access inside the function
    and also outside of the function.
'''


# Local variable

def local_val():
    x = 100
    print(x)

# print(x) # can't access as x is local 
local_val()


# Global variable
name = 'shakir'
def global_var():
    print(name)

print(f'Through Global variable {name}')
global_var()


# changing the Global variable
count = 0

def update():
    global count # Global keyword is used always
    count += 1
    print(count)

print(count)
update()

