# Type Casting in python
'''
Converting Variable from One data type to another,
python used the dynamicaly variable,
can't add 'string + integer',

'''

number = '10'
# print(number + 5 ) # not possible 

num = int(number) # change str to integer
print(num + 5 ) # not possible


price = 9.99
price_int = int(price)  # Drops decimal
print(price_int)  # 9

num1 = '3.14'
num2 = float(num1)
print(num2 + 1)
