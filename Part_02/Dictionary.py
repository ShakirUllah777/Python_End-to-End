'''
Dictionary
A data structure that store value in Key-value-pairs
student = {
    "name": "Ali",
    "age": 22,
    "course": "Python"
}
'''

# Problem -- using list to store multiple items
student = ["Ali", 22, "Python"] # do't which value represnt which

# Solutions
student = { 
    "name": "Ali",
    "age": 22,
    "course": "Python"
} # now data is structure and readable 



# Some Important Methods of Dic
'''
| Method   | Purpose                 |
| -------- | ----------------------- |
| keys()   | returns all keys        |
| values() | returns values          |
| items()  | returns key-value pairs |
| get()    | access value safely     |
| update() | update dictionary       |
| pop()    | remove item             |
| clear()  | remove all items        |
'''