# Conditionals in python

# Allow the programmer to make the decesions
# mostly used contitionals are 
# IF, Else If, Else 


# If -- Statment -- run if condtion id true
# syntax for IF statment is 
# if Condition:
#    code

if 5 > 2:
    print('5 is grater then  2!')

# 2.  
# If - Else 
# If the condition is False then rn this
age = 20
if age > 21: #condition us not True Here
    print('You are adult!')
else: # This will run 
    print('You are not Adult!')

# 3.
# If - Elif - Else
# used when there are 'Multiple Conditins'

marks = 89

if marks > 90: # 1st Check this.
    print('Grade A.')
elif marks > 80: # 2nd check this.
    print('Grade B.')
else: # if all above are fail then run this.
    print('Grade C.')


#Comparison Operators (Used in Conditions)
# | Operator | Meaning          |
# | -------- | ---------------- |
# | `==`     | equal            |
# | `!=`     | not equal        |
# | `>`      | greater than     |
# | `<`      | less than        |
# | `>=`     | greater or equal |
# | `<=`     | less or equal    |


# Logcal Operation in Loops
age = 21
citizen = True

if age > 18 and citizen: # Both need to correct
    print('Okay! Let him Go.')
else:
    print('One Condtion need to b Correct!')

if age > 30 or citizen: # atlest one need to correct
    print('Okay! Let him Go.')
else:
    print('None of the above Match!')