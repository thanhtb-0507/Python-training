"""
dictionary is a collection, ordered, changeable, 
							no-duplicates
key: unique, immutable
value: free baby
{key:value, key:value}
"""
a = {}
print(type(a))
# <class 'dict'>

d = {1:'a', 2:"what the fooboo"}
print(type(d))
print(d)
# {1: 'a', 2: 'what the fooboo'}

# d = dict(('name','Anby'), ('element','electric'))
# TypeError: dict expected at most 1 argument, got 2
# chú ý dấu [] hoặc {} khi tạo bằng dict()
d = dict({("name","Anby"), ("element","electric")})
print(d)
# {'element': 'electric', 'name': 'Anby'}

# using <dict>[key] will cause error when key not exsist
# using get(<key>) will return null when key not exsist

d["type"] = "disorder"
print(d)
# {'element': 'electric', 'name': 'Anby', 'type': 'disorder'}

d["name"] = "Grace"
print(d)
# {'element': 'electric', 'name': 'Grace', 'type': 'disorder'}

# <dict>.pop(<key>)
# <dict>.popitem() remove and return the last index
# <dict>.clear() 
# del <dict>

print(d.pop("name"), '\n', d)
# Grace
#  {'element': 'electric', 'type': 'disorder'}

print(d.popitem(), '\n', d)
# ('type', 'disorder')
#  {'element': 'electric'}

# pop() just return value
# popitem() return both value and key!

# <dict>.copy()
dd = d.copy()
print(dd)

# dict.fromkeys(<keys>, <value>)
d = dict.fromkeys((1, 2, 3))
print(d)
# {1: None, 2: None, 3: None}

d = dict.fromkeys({1, 2, 3},["ichi", "ni", "san"])
print(d)
# {1: ['ichi', 'ni', 'san'], 2: ['ichi', 'ni', 'san'], 3: ['ichi', 'ni', 'san']}

# d = dict.fromkeys({1, 2, 3},"ichi", "ni", "san")
# TypeError: fromkeys expected at most 2 arguments, got 4

# Kết luận: fromkeys tạo được nhiều key nhưng tất cả chung value

d = dict.fromkeys((1, 2, 3))
print(d.items())
# dict_items([(1, None), (2, None), (3, None)])

print(d.values())
# dict_values([None, None, None])

print(d.keys())
# dict_keys([1, 2, 3])

print(d.setdefault(1))
# None

print(d.setdefault(4, "None?"))
# None?
print(d)
# {1: None, 2: None, 3: None, 4: 'None?'}

# <dict>.update({<key>:<value>})
# all(<dict>)
# any(<dict>)
# len(<dict>)
# sorted(<dict>) # sap xep list key va tra ve

# <> in <> # ktra co key trong dict