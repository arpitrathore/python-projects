## Notes

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