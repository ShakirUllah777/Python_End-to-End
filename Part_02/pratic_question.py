'''
1️⃣ User Input + Type Casting
Write a program that:
asks the user to enter two numbers
converts them to integers
prints:
sum
multiplication
division
Handle the case where the user enters non-numeric values.
'''

try:
    num1 = int(input('Enter a 1st number: '))
    num2 = int(input('Enter a 2st number: '))

    print(num1 + num2)
    print(num1 * num2)
    print(num1 / num2)
except ValueError:
    print('Invalid Value')



'''
2️⃣ Exception Handling
Write a program that:
asks the user to enter a number
prints its square
If the user enters something invalid (like a string), handle the error using try-except.
'''

try:
    number = int(input('Enter a number: '))
    square = number * number
    print(f'Squre of number is {square}')
except Exception as e:
    print(e)


'''
3️⃣ Function + List
Create a function called:
find_max(numbers)
The function should:
take a list of numbers
return the largest number
do not use max()
'''

def find_max(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest

my_list = [1,10,3,4,5]
max_value = find_max(my_list)
print(f'Max number in this list is: {max_value}')


'''
4️⃣ List Processing
Write a program that:
asks the user to enter 5 numbers
stores them in a list
prints:
the largest number
the smallest number
the sum of all numbers
'''

numbers = []
print('Enter 5 Numbers:')
for i  in range(1,6):
    num = int(input(f'Enter {i} number: '))
    numbers.append(num)


print(f'Largest: {max(numbers)}')
print(f'Smallest: {min(numbers)}')
print(f'Sum: {sum(numbers)}')


'''
5️⃣ Tuple Unpacking
Create a tuple:
student = ("Ali", 22, "Python")
Write a program that:
unpacks the tuple into three variables
prints each value separately.
'''
student = ("Ali", 22, "Python")
name , age , skill = student

print('Tuple Unpacking values are: ')
print(f'Name is: {name}')
print(f'Age is: {age}')
print(f'Skill is: {skill}')


'''
7️⃣ Remove Duplicates
Write a program that:
takes a list with duplicate numbers
removes duplicates using a set
converts it back to a list
prints the final list.
'''

dup_list = [1,2,3,4,5,1,2,3,4,5]
print(dup_list)
conv_set = set(dup_list)
print(conv_set)
con_list = list(conv_set)
print(con_list)


'''
1️⃣2️⃣ List + Function
Create a function:
count_even(numbers)
The function should:
take a list of numbers
return how many even numbers exist in the list.
'''

def count_even(numbers):
    count_even_list = []
    for i in numbers:
        if i % 2 == 0:
            count_even_list.append(i)
    return len(count_even_list)

my_list = [1,2,3,4,5,6,7,8,9,10,2,4,6]
list_total_even = count_even(my_list)
print(f'Total Even number in your List are: {list_total_even}')


