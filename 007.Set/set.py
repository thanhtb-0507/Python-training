mind_set = {'not lazy', 3, 3, 4, 4, 1, 9, 8, 7, 8}
print(mind_set)
'''
{1, 'not lazy', 3, 4, 7, 8, 9}
	Set does not allow multiple instance of an value
	and also rearrange/sort follow the value

	>> why 'not lazy' is in the middle of 1 and 3?
'''

haizz = {}
print('haizz is ', type(haizz))
# haizz is  <class 'dict'>

haiz = set()
print('haiz is ', type(haiz))
# haiz is  <class 'set'>

# SINGLE element only
haiz.add("@")
print(len(haiz))

haiz.clear()
# haiz.update(1, 2, 3, 4, 5, 6, 7, 8)
# 'int' object is not iterable

haiz.update([1, 2, 3, 4, 5, 6, 7, 8]) 
# update only use set/list/tuple
print(len(haiz))
# 8

haiz.discard(9)
# nothing happend

# haiz.remove(9)
# KeyError: 9 cause remove()

haiz.discard(7)
print(haiz)
# {1, 2, 3, 4, 5, 6, 8}

haiz.remove(1)
print(haiz)
# {2, 3, 4, 5, 6, 8}

for x in range(6):
	print(haiz.pop())

"""
2
3
4
5
6
8
"""

s = {1, 2, 3}
a = s.copy()
print(a)
# {1, 2, 3}

s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.difference_update(s2)
print(s1)
# {1, 2}

s1.intersection_update(s2)
print(s1)
# set() # null set?

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {2, 3}
s4 = {6, 7}

print(s4.isdisjoint(s2))
# True
print(s3.isdisjoint(s1))
# False
print(s3.issubset(s1))
# True
print(s1.issuperset(s3))
# True
s1.symmetric_difference_update(s2)
print(s1)
# {1, 2, 4, 5}

A = {1, 2, 3, 4}
B = {4, 5, 6, 7}

print(A|B)
# {1, 2, 3, 4, 5, 6, 7}
A.union(B)
print(A)
# {1, 2, 3, 4}
print(A.union(B))
# union() and | does not effect the set

print(A&B)
print(A.intersection(B))
print(B.intersection(A))

# difference: A - B, A.difference(B)
# .symmetric_difference(), A ^ B

print(1 in A)
# True
print(1 in B)
# False

# all() kiem tra set null, hoac 0 thi false
# any() kiem tra co phan tu hay k
# len()
# max() min() lay min, max cua set
# sorted()
# sum() tong cua set

# frozenset()

s1 = {1, 2, 3}
# s1.frozenset()
# 'set' object has no attribute 'frozenset'
s1 = frozenset(s1)
print(type(s1))