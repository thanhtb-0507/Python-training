empty_list = []
print(empty_list)
# []

bla = [1, 2, 3]
print(bla)
# [1, 2, 3]

mixed = ['dafu', 'CircleK', 39]
print(mixed)
# ['dafu', 'CircleK', 39]

list_of_list = [['a', 1], ('tuple', 2), [2,3] ]
print(list_of_list[2][1])
# 3

var001 = [1]
print('var001 is ', type(var001))
# var001 is  <class 'list'>

var002 = [1, ]
print('var002 is ', type(var002))
# var002 is  <class 'list'>

bla.append(4)
print(bla)
# [1, 2, 3, 4, 4, 5]

bla.extend([4, 5])
print(bla)
# [1, 2, 3, 4, 4, 5]

# triple the bla list
bla = bla * 3
print(bla)
# [1, 2, 3, 4, 4, 5, 1, 2, 3, 4, 4, 5, 1, 2, 3, 4, 4, 5]

del bla[3]
print(bla) 
# [1, 2, 3, 4, 5, 1, 2, 3, 4, 4, 5, 1, 2, 3, 4, 4, 5]

del bla[5:]
print(bla)
# [1, 2, 3, 4, 5]

# bla.push(6)
# print(bla)
bla.pop()
print(bla)
# [1, 2, 3, 4]

bla.remove(2)
print(bla)
# [1, 3, 4, 5]

bla.clear()
# bla[:] = [] # is the same
print(bla)
# []

bla = [1, 2, 3, 4, 5, 6]
bla[2:3] = []
print(bla)
# [1, 2, 4, 5, 6]

bla.insert(2, 3)
bla[2] = []
print(bla)
# [1, 2, [], 4, 5, 6]

bla.pop(2) # remove and return value at index 2
bla.insert(2, 3)
print(bla)
# [1, 2, 3, 4, 5, 6]

bla.reverse()
print(bla)
# [6, 5, 4, 3, 2, 1]

bla.reverse()
bla + [7, 8, 9, 10] 
# just effect the interpreter, no effect on bla list
print(bla)
# [1, 2, 3, 4, 5, 6]

blaa = bla # dafu just like pointer in c; deep copy
blaa += [7, 8, 9, 10]
print(bla)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

blab = bla[:] # shallow copy
blab[5:] = []
print(bla)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nested_l = [bla, blaa, blab]
print(nested_l)
''' 
[	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
	[1, 2, 3, 4, 5]]
'''



"""NOTICE:
only str get to + each other
	File "/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/005.List/list.py", line 14, in <module>
	    print('var001 is ' + type(var001))
	TypeError: can only concatenate str (not "type") to str

append() can only take in one argument thus ...
	Traceback (most recent call last):
	  File "/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/005.List/list.py", line 21, in <module>
	    bla.append(4, 5)
	TypeError: list.append() takes exactly one argument (2 given)

list but no push, lame
	Traceback (most recent call last):
	  File "/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/005.List/list.py", line 33, in <module>
	    bla.push(6)
	AttributeError: 'list' object has no attribute 'push'



"""