'''
1️⃣ Introduction: What is Generator Expression?
A generator expression is similar to list comprehension, but instead of creating a full list in memory, it generates values one by one (on demand).
👉 Simple definition:
Generator = produces values one at a time instead of storing all at once
👉 Difference:
    [] → list
    () → generator
'''

# Problem 
# List Comphression store all values at once in the memory 
# which take a lot of memory


# Solution 
# Generator Expression
# Value Generate when needed
gen = ( i **2 for i in range(1,6))
print(gen)
for van in gen:
    print(van)

'''
7️⃣ Real-Time Example (Backend / API)

Imagine you receive millions of user records, and you only want emails.

❌ List (bad for large data)
emails = [user["email"] for user in users]
✅ Generator (better)
emails = (user["email"] for user in users)

👉 Emails are processed one by one, not stored fully.
'''