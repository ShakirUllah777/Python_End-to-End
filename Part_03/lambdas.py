'''
Lambda Function in Python.
Concept:
    A lambda function is a small anonymous function.
    Anonymous means a function without a name.
    It can have any number of arguments, but only one expression.

lambda arguments : expression
'''

# Problem 
# some time we need a function once and writeing full function is unnecessary
def squre(x):
    return x * x

print(squre(2))

# Solution
squre = lambda x: x * x
print(squre(4))

# With 2 arguments
add = lambda a, b: a + b
print(add(10,20))

# Lambda with map() function apply to each element in list
numbers = [1,2,3,4,5]

result = list(map(lambda x: x * 2, numbers))
print(result)

# Lambda filt filter() function
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number = list(filter(lambda x: x % 2 == 0, numbers))
print(f'Even number from list are: {even_number}')
