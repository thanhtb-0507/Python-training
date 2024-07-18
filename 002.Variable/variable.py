#Assigning varialbes
x = 5
y = "Coder"
print(x)
print(y)

print()

#Change type
z = 100
z = "a hundred"
print(z)

print()

#Assigning multiple variable
a, b, c = 5, 3.2, "Hello"
print (a) #5
print (b) #3.2
print (c) #Hello

print()

a = b = c = "same"
print (a) #same
print (b) #same
print (c) #same

"""
variable name cannot start with number!!
Can only contain alphabet-numerric character and underscores (_)
Case sensitive
"""

print()

abc, Abc, ABC = 1, 2, 3
print(abc)
print(Abc)
print(ABC)

print()

var = 12
print(type(var))
print(var, " is integer?", isinstance(var, int))
print(var, " is string?", isinstance(var, str))

print()

import constant
print(constant.PI)
print(constant.GRAVITY)
print(constant.TBT)
constant.TBT = 1
print(constant.TBT)

"""
This show that there is actually no const/constant in python
The act of create a constant.py is just in agreement!!
"""


"""OUTPUT:
5
Coder

a hundred

5
3.2
Hello

same
same
same

1
2
3

<class 'int'>
12  is integer? True
12  is string? False

3.14159265
9.8
BAKAYARO
1
"""