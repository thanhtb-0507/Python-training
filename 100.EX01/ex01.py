"""
Python practice bai 1:
author: Tran Ba Thanh
date: 17/07/2024

remaining proplem:
	- no checking for the name and score
	- not yet private variable
	- using list insted of dict
	- yet to have error handler
	- still C code mindset
"""

# import 

# class definition
class STUDENT(object):
	"""
	A class to represent a student.
	Each student have 3 variable: 
		(str)name for their name
		(int)m for their math score
		(int)l for their literature score
		(int)e for their english score
		(float) for their average score
	Brief about this class's function:
	"""
	avg = 0.0

	def __init__(self, name = "", m = 0, l = 0, e = 0): # m 
		super(STUDENT, self).__init__()
		self.name = name
		self.m = m
		self.l = l
		self.e = e
		self.avg = round((m + l + e)/3, 1)

	# function to update private variable
	# def update_m(m)
	# 	_m = m
	# def update_l(l)
	# 	_l = l
	# def update_e(e)
	# 	_e = e
	# will make it private in the near future


	def student_info(self):
		return (f"name: {self.name}, toan: {self.m}, "
				f"van: {self.l}, anh: {self.e}, avg: {self.avg}")

class LIST_STUDENT(STUDENT):
	"""
	Class to create list of student
		(list)lists: student list of a class
		(int)num: number of student in class
	Brief about this class's function:
	"""
	def __init__(self, lists = [], num = 0):
		super(LIST_STUDENT, self).__init__()
		self.lists = lists
		self.num = num

	# input student info = input_s_i
	def input_s_i(self):
		if (self.num == 0):
			num_correct = False
			while (num_correct == False):
				self.num = int(input("Number of student: "))
				if (self.num < 0):
					print("Value is invalid! Please re-enter the value.")
				else:
					num_correct = True
			del num_correct

		for i in range(self.num):
			print("Input info for student no.%d:"%(i))
			num_correct = False
			while (num_correct == False):
				name = str(input("Name: "))
				m = input("Math      : ")
				e = input("English   : ")
				l = input("Literature: ")
				if not ((0 <= int(m) <= 10) | 
						(0 <= int(e) <= 10) | 
						(0 <= int(l) <= 10) |
						(name != "")):
					print("Value is invalid! Please re-enter the value.")
				else:
					num_correct = True

			self.lists.append(STUDENT(name, int(m), int(l), int(e)))

	# return the index of the student who has highest avg
	def highest_avg(self):
		hi = 0
		max = self.lists[0].avg
		for i in range(len(self.lists)):
			if self.lists[i].avg >= max:
				max = self.lists[i].avg
				hi = i
		return hi

	def name_hi_avg(self):
		hi = self.highest_avg()
		hi_list = []
		for i in range(len(self.lists)):
			if self.lists[i].avg == self.lists[hi].avg:
				hi_list.append(self.lists[i].name)
		return hi_list


# main program
classA1 = LIST_STUDENT()
classA1.input_s_i()

print("b)")
hi = classA1.highest_avg()
print(classA1.lists[hi].avg)

print("c)")
for i in range(len(classA1.lists)):
	print(classA1.lists[i].student_info())

print("d)")
hi_list = classA1.name_hi_avg()
print(hi_list)

"""OUTPUT:
Number of student: 2
Input info for student no.0:
Name: ngoc
Math      : 3
English   : 4
Literature: 5
Input info for student no.1:
Name: thao
Math      : 6
English   : 7
Literature: 8
b)
7.0
c)
name: ngoc, toan: 3, van: 5, anh: 4, avg: 4.0
name: thao, toan: 6, van: 8, anh: 7, avg: 7.0
d)
['thao']
"""