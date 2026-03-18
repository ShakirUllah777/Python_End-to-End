'''
Context Manager;
    with ---- automaticaly handles the setup and cleanup for 
    resources, ensure they are propley handle if the error occures,

'''

# Problem 
file = open('data.txt', 'r')
data = file.read()
print(data)
file.close() # close the file alwasys

# some time if we forget to close() the file it will stay open
# can cause the memory leake 

# Solution ---- With
with open('data.text', 'r') as file:
    data = file.read()
    print(data)

# file is automaticly closed
# Safer and cleaner
# Hanldes error propely

