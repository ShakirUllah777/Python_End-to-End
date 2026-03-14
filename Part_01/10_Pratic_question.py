'''
1️⃣ String Length
Write a program that:
asks the user to enter a word
prints the length of the word
'''
a = input('Enter a word: ')
print(len(a))

''' 
2️⃣ First and Last Character
'''
name = 'shakir'
print(name[0])
print(name[-1])

''''
3️⃣ Convert Sentence to List
'''
a = input('Enter a sentence of atlest 5 character: ')
print(a.split(' '))

'''
4️⃣ Count Characters Using Loop
'''
word = 'Programming'
count = 0
for char in word:
    count += 1
print(count)


'''
5️⃣ Even or Odd Number
'''
num = int(input('Enter a Number: '))

if num % 2 == 0:
    print('Even Number')
else:
    print('Odd Number!')

'''
6️⃣ Print Numbers Using Loop
'''
for i in range(11):
    print(i)

'''
8️⃣ Check Word in List
'''
fruits = ["apple", "banana", "mango"]
fru = input('Enter a Fruit Name: ')

if fru in fruits:
    print('Fruit found')
else:
    print('Not Found!')


'''
🔟 Count Words in a Sentence

Write a program that:
takes a sentence from the user
uses split() to convert it into a list
prints how many words are in the sentence
'''

cun_wods = input('Enter a sentence of your Choice: ')
cun_split = cun_wods.split()
print(len(cun_split))