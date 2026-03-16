'''
Iterator:
An iterator is an object that lets you go through elements one by one.
'''


'''
Problem
Wnat to access each element of the list 
so need to access one by one is hard 
[10,20,30,40]
10 -> 20 -> 30 -> 40
'''


# Solution 
# we can used the Iterator go throug each item in list 

mylist = [10,20,30,"hary", 'ali']

for i in mylist:
    print(i)


it = iter(mylist)
print(next(it))
print(next(it))
print(next(it))


'''
Used:
    we used in loop to take the items for the database,
'''