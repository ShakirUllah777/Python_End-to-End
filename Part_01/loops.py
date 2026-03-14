# Loops in Python.
''' Used to repeat a block of code multimple time 
unitl the conditon is flase or items in the sequence 
are processed 

--- Avoid writing same code agian and again

'''
# Loops in python 
# 1. For Loop
# 2. While Loop

# 1. For Loop 
# used to iterate over the sequences
# syntx is 
# for variable in sequence:
#      code 
for i in range(5):
    print(i)

fruits = ['Apple', 'Chery' , 'Mango']
for fruit in fruits:
    print(fruit)

print(max(fruits))
print(min(fruits))

# 2. While Loop
# Run as long as Conditon is True

i = 1
while i < 5:
    print(i)
    i += 1


