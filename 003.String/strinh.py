var1 = 'Hello Warudo!'
var2 = "Python programing"
var3 = '''Hello the people 
			of the world'''
my_string = """Hello, welcome to
the world of Python"""

print(var1)
print(var2)
print(var3)
print(my_string)

"""
Both triple ' and " can be use for multi-line comment
and for multi-line print.
Its just a little sheesh for multi-line print.
"""

print("I\'m \"not\" suck")
print("Is it \"like\" C?\nyehhh")
print(r'/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/001.First_program')
print(r'D:\TAI_LIEU\ET-E9\Program\Naitei\Intern\project\001.First_program')

var1 = "ha"
print(var1 * 3)
var2 = "hohoho"
print(var1 + var2)

name = "Jotaro"
print("Hello " + name + ", I\'m your father")
msg = f'Hello {name}, I\'m your father'
print(msg)
print(f"Hello {name}, can u hear me")
print(f"Hello %s, can u hear me"%(name))
name = input("your name:")
print("Hello {vl}, can u hear me".format(vl = name))

from string import Template
new = Template('Hello $name, can u hear me')
print(new.substitute(name = name))

print(name[0])		#index tu trai sang phai
print(name[-2])		#index tu phai sang trai voi index < 0
print(name[1:4]) 
#[start:stop]
#Khong tinh ky tu so 4, Mario thanh ari!1
#string k cho sua gia tri :( -> gan chuoi moi!!

name 
"""	dong nay hnhu khong co tac dung, 
	chi co tac dung voi terminal"""
# del name
# name

#mot so phuong thuc lam viec voi chuoi
msg = "I love anime, not Python"
print(len(msg))
print(msg.lower())
print(msg.upper())
a0, a1, a2, a3, a4 = msg.split()
aa = msg.split()
print("a1 = %s"%(a1))
# print("aa = %s"%(aa))
a = msg.find("anime")
print(a)
a = msg.find("sus")
print(a)
msg1 = msg.replace('anime', 'game')
print(msg1)
# print(msg1 = msg.replace('anime', 'game'))
# vua khai bao vua print gay loi
print("msg = %s"%(msg))

'''OUTPUT:

'''