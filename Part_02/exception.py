# Excepions in Python 
'''
Problem:
   some time if there is any mistake in code then we get 
   the error and code break and program stop, that is not
   got habit.
Solution:
    1. Prevent Program when From crashing when an error occur
    2. Provide meaningfull message
    3. Handle unexpected situations , file not fount
'''

# Simple Approch
age = int(input('Enter you age: '))

if age < 0:
    print('Age can not b Negative')
else:
    print('age is positive:')


# exception Approch 
try:
    age = int(input('Enter Your age: '))
    if age < 0:
        raise ValueError('Age canot be Negative')
except ValueError as e:
    print(f'Invalid Input {e}')
