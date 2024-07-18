"""logical condition
==	<=	>=	>	<	!=	
"""
d = "baka"
if d == "baka":		# chú ý dấu ":" do trong c không dùng!!!!
	d += " yarou"
	print(d)

a, b = 3, 3
if b > a:
	c = "tehehe"
elif a == b:
	c = "haha"
else:
	c = "yamete"

print(c)

if "haha" == c: c = "Python"

print(d) if ("haha" == c) else print(f"enough {c} yet?")

# and, not, or thay cho &&, !<>, ||

# while use when doesnt known how many times to repeat
i = 0
while i < 10:
	print(' ' * (10 - i), '*' * (2 * i + 1))
	i += 1
else:
	# a = [1, 2, 3]
	# for ii in a:
	# better below:
	# for ii in range(3): # range(<stop>) # start = 0 and gap = 1
	for ii in range(0,3,1): # range(<start>, <stop>, <gap>)
		print(' ' * 9, "|||")

# range(len(<smt>))
# for <>:
#	 <>
# else:
# 	 <>

# break
# 	the else clause is not execute if terminated by a break!!
# continue
# pass = _asm(nop)

"""match: just like switch case
match status:
	case 400:
		return "Bad request"
	case 401:
		return "UNDEAD - Yoasobi"
	case 402 | 403 | 404:
		return "or is okay"
	case 405 if <>:
		print("guard is evaluated after value capture")
	case _:
		return "something"
"""

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")