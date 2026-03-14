# String ---- Important part bcx text is used eveyWhere

# Strings represent text data and are written inside quotes.
name = 'Shakir'
course = 'Python'
message = ''' This is multiline
string string 
in the python '''


# Accessing Characters (Indexing)
print(name[0])
print(name[1])
print(name[-1])
print(name[-2])

# String Silicing
# when we wnat to extrach some Portion of the string
# string[str:end]

word = 'PrograMMing'
print(word[0:7])
print(word[:7])
print(word[7:])

# String Concatation
# uset to 'Join two or more Strings'
a = 'shakir'
b = 'Turk'
result = a + ' ' + b # if b is other type then --- TyprError
print(result)
print(len(a))

# Buildin common sting Methods
print(word.upper())
print(word.lower())
print(word.title())

name = '     harry   '
print(name.strip()) # used to remove spaces

data = 'Apple,Bnana,Orange'
res = data.split(',')
print(res)
print(type(res))