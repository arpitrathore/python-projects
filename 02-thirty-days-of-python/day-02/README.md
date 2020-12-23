## Notes : Day-02
### Topic : Numbers, variables and strings

### 1. Python documentation 
Link : [link](https://docs.python.org/3.8/tutorial/introduction.html)

### 2. Special variable '_' in iteractive mode
In interactive mode, the last printed expression is assigned to the variable underscore '_'.
<br><br>
This variable should be treated as read-only by the user. Don’t explicitly assign a value to it — you would create an independent local variable with the same name masking the built-in variable with its magic behavior
```
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
```

### 3. Raw strings
If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:
```
>>> print('C:\some\name')  # here \n means newline!
C:\some
ame
>>> print(r'C:\some\name')  # note the r before the quote
C:\some\name
```

### 4. Triple quotes
String literals can span multiple lines. One way is using triple-quotes: """...""" or '''...'''. End of lines are automatically included in the string, but it’s possible to prevent this by adding a \ at the end of the line. The following example:
```
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
```

### 5. Slices
One way to remember how slices work is to think of the indices as pointing between characters, with the left edge of the first character numbered 0. Then the right edge of the last character of a string of n characters has index n, for example:
```
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

>>> word[:2]   # character from the beginning to position 2 (excluded)
'Py'
>>> word[4:]   # characters from position 4 (included) to the end
'on'
>>> word[-2:]  # characters from the second-last (included) to the end
'on'
```

### 6. Strings are immutable
Python strings cannot be changed — they are immutable. Therefore, assigning to an indexed position in the string results in an error:
```
>>> word[0] = 'J'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>> word[2:] = 'py'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

### 7. Length of string
```
>>> s = 'supercalifragilisticexpialidocious'
>>> len(s)
34
```