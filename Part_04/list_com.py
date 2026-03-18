'''
List Comprehension,
method to write the list code in one line

Probleme
    writing multiple line of code 
Solution
write one line of code
'''

# # Method one
# squre = []
# for i in range(1,6):
#     squre.append(i ** 2)

# print(squre)

# # Method Two 
# # list comphression 
# squre1 = [ i **2 for i in range(1,6)]
# print(squre1)


# sentences = [
#     "I love Python programming",
#     "JavaScript is popular",
#     "Python is great for AI",
#     "I like Java"
# ]

# # simple code
# for s in sentences:
#     if 'Python' in s:
#         print(s)

# # list comphresion
# python_sentence = [s for s in sentences if 'Python' in s]
# print(python_sentence)


# Pratic Question List Comphresion
squres = [i **2 for i in range(1,21)]
print(squres)

nums = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [i for i in nums if i % 2 == 0]
print(even_numbers)

names = ["Ali", "Ahmed", "Usman", "Ayesha", "Bilal"]
first_leter = ['A']
first_leter_filter = [ name for name in names if (name[0] in first_leter)]
print(first_leter_filter)

ages = [12, 25, 17, 30, 15, 22]
age_grater = [ age for age in ages if age > 18]
print(age_grater)

nums = [1,2,3,4,5,6,7,8,9]
square_odd_numbers = [i **2 for i in nums if i % 2 != 0]
print(square_odd_numbers)


words = ["apple", "bat", "banana", "cat", "orange"]
words_length = [ i.upper() for i in words if len(i) > 4 ]
print(words_length)
