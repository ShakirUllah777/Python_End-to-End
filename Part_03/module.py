'''
Module in Python
File That coantion sume function, variable and classes 
that can be used in some other Program file.
save as file_name(module_Name.py)

Problem:
    if u writen every thing in one file code become to large and messay
Solution:
    split the code into multiple files
'''

# Example
import math # python buildin module
from math import factorial

print(math.sqrt(25))
print(factorial(5)) # used buitin module


# Cuntome made module
import custome_module

custome_module.greet('Shakir')
print(custome_module.add(1,2))


'''
In real word system we used for this,
Models -- databases logic
custome logic
main.py
database.py
auth.py
like this we used them
'''