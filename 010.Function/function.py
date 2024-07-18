def afunction(smt):
	"""This function create for \ntrying out function"""
	print("Man, I\'m to used to printf. " + smt)

afunction("Get me back to C.");
# Man, I'm to used to printf. Get me back to C.

print(afunction.__doc__)
# This function create for
# trying out function

def error_code_reading(error_code):
	"""This function return the meaning of error code"""
	match error_code:
		case 400:
			return "Bad request."
		case 401:
			return "Unauthorized."
		case 404:
			return "Not found."
		case _:
			return "Something else."

print(error_code_reading(404))
# Not found.
print(error_code_reading(504))
# Something else.

# def try_default_argument (a1, a2, a3 = 'lol', a4)
# SyntaxError: non-default argument follows default argument
def try_default_argument (a1, a2, a3 = 'lol', a4 = "olo"):
	print (a1 + a2 + a3 + a4)

# try_default_argument()
# TypeError: try_default_argument() missing 2 required positional arguments: 'a1' and 'a2'
try_default_argument('h','e','l','l')
try_default_argument(a2 = "lolo", a1 = "lololo")

def synapse(**connection):
	print("connected at", connection["one"])

d = {1:5, 2: 255}
# synapse(d)
# TypeError: synapse() takes 0 positional arguments but 1 was given
# synapse(**{1:5, 2: 255})
# TypeError: keywords must be strings
#keyword argument or kwarg can only be str in this case?

d = {"one":5, "two": 255}
synapse(**d)
# connected at 5

# lambda funct as an anoynimous funct in def funct
def myfunc(n):
	return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(3))
# 6
	
def foo():
	x = 20
	def bar():
		global x
		x = 25

	print("Before calling bar: ", x) # x = 20
	print("Calling bar now")
	bar()
	print("After calling bar: ", x) # x = 20
   
foo()
print("x in main : ", x) # x = 2
