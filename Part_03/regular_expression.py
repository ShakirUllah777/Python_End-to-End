'''
Regular Expression.
    sequnce of character that forms search operations.
    used to check if the string conation specific character.

import re # build in module by python

'''

# Important Regular Expression mostly used!
'''
| Pattern | Meaning         | Example         |
| ------- | --------------- | --------------- |
| `.`     | any character   | `a.b`           |
| `\d`    | digit           | 0-9             |
| `\w`    | word character  | letters/numbers |
| `\s`    | space           | whitespace      |
| `+`     | one or more     | `\d+`           |
| `*`     | zero or more    |                 |
| `^`     | start of string |                 |
| `$`     | end of string   |                 |

'''

import re 
phone = '1234567891010'

if re.match(r"\d{11}", phone):
    print("Valid number")
else:
    print("Invalid")


text = "Contact me at test@gmail.com"

email = re.findall(r"\S+@\S+", text)

print(email)