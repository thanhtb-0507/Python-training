"""Decorators
Everything is obj.
Assign funct to variable is possible :V

"""

"""funastyness
a = some_function
print(a) 
# return the address of function a
# also a is now a function
# note that some_function is without the ()

print(a())
# execute the function some_function() that funct a pointed to.

also passing function around like a variable so u dont need
the ()
only when using it, executing it u need the ()
"""

from functools import wraps


def func_a():
	return "yahalo"

a = func_a()
print(type(a)) # what ever the func_a return!
print(a)

b = func_a
print(type(b))
# <class 'function'>
print(b)
# <function func_a at 0x7f412f982440>
print(b())
# yahalo

def huger(func):
	@wraps(func)
	def hugging():
		print("tehehe x 3")
		func()
		print("tehehe x 3.14")
	return hugging
	# return a function

def want_hug():
	print("tihihi")
	"""
		File "/mnt/d/TAI_LIEU/ET-E9/Program/Naitei/Intern/project/014.Decorators/decorators.py", line 45
		def want_hug()
		          ^
		SyntaxError: expected ':'
	"""
want_hug()
# tihihi

want_hug = huger(want_hug)

want_hug()
# tehehe x 3
# tihihi
# tehehe x 3.14

# basicly for convinitent
# people create and use @
@huger
def want_hugg():
	print("graw!")

want_hugg()
print(want_hugg.__name__)
# with wraps: want_hugg
# without	: hugging