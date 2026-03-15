'''
List
Data structure used to store Multiple value in single variable
List arr:
    ordered
    mutabale (changeable)
    can store different type data
'''

# Problem 
# we wnat to store the multiple Fruits 
a = 'Apple'
b = 'Banan'
c = 'chery'
# print(a,b,c)

# Solution -- using the List
fruits = ['Apple','Banna','chery']
# print(fruits)

# Prperties of the List

# Ordered 
numer = [1,2,3,4]
# Allow the Duplicate 
numbers = [1,1,1,2,2,21]

# Accesing elements
print(fruits[1])
print(fruits[0])

# List Slicing
print(numbers[1:4])

# Adding element to list
fruits.append('Kela')

# can store multiple data type items
mul_items  = ['Apple', 21 , 21.1]


# Others all Method of the List
'''
| Method      | Purpose            |
| ----------- | ------------------ |
| `append()`  | add element        |
| `insert()`  | add at index       |
| `extend()`  | add multiple items |
| `remove()`  | remove element     |
| `pop()`     | remove by index    |
| `clear()`   | remove all items   |
| `index()`   | find index         |
| `count()`   | count occurrences  |
| `sort()`    | sort list          |
| `reverse()` | reverse list       |
| `copy()`    | copy list          |
'''