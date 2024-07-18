"""
r	reading
w	write, create, truncate
x	create, error if file exist
a 	appending at the end w.o/truncate, create
t 	text mode (default)
b	binary mode
+	updating (read & write)
"""

import os
print(os.getcwd(), '\n')
# runing python in wsl:
# 	/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/015.Files
# runing python in native windows:
# 	D:\TAI_LIEU\ET-E9\Program\Naitei\Intern\project\015.Files
print(os.listdir("/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/015.Files/"))

'''
# open(file, mode='r', buffering=-1, encoding=None, 
#  errors=None, newline=None, closefd=True, opener=None)
f = open("test.txt", 'w')

print(type(f))
# <class '_io.TextIOWrapper'>

f.close()
'''

with open("test.txt", 'w') as f:
	f.write("Boukoyara!\nBakayarou!") # this also return number of char written

print("Is file closed? ", f.closed)		# True

with open("test.txt", 'r') as ff:
	print(ff.read())
print("Is file closed? ", ff.closed)	# True


"""
try:
	f = open(...)
finally:
	f.close()

with open(...) as f:
	f.write(...)

"""
