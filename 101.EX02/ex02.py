"""
Python practice bai 2:
author: Tran Ba Thanh
date: 17/07/2024

remaining proplem:
	- take a long time to write
"""

# import
import sys

# exception
class format_err(Exception):
	"""docstring for format_err"""
	def __init__(self):
		self.message = "Time must be in hh:mm format."
		super().__init__(self.message)
		
class time_err(Exception):
	"""docstring for time_value_err"""
	def __init__(self):
		self.message = "Time value error."
		super().__init__(self.message)
		


# class definition
class time(object):
	"""docstring for time"""
	def __init__(self, hh = 0, mm = 0):
		super(time, self).__init__()
		self.hh = hh
		self.mm = mm
		self.hf = 0.0

	def str_to_time(self, str_time):
		hh, mm = [int(i) for i in str_time.split(":")]
		self.hh = hh
		self.mm = mm
		# maybe not a good idea but ...
		self.hf = round((hh + (mm/60)), 1)

	def update_hf(self):
		self.hf = round((self.hh + (self.mm/60)), 1)

	def print_time(self):
		return f"{self.hh}:{self.mm}"
		

# function definition
def cal_OT(t1, t2):
	"""
	Calculate OT, takes in check-in, check-out as class(time).
	"""
	t3 = time()
	if(t2.mm > t1.mm):
		t3.hh = t2.hh - t1.hh
		t3.mm = t2.mm - t1.mm
		t3.update_hf()
		return t3.hf
	else:
		t3.mm = (60 - t1.mm) + t2.mm
		t3.hh = t2.hh - t1.hh - 1
		t3.update_hf()
		return t3.hf
"""
14:15
08:45
06 but minus 1
05:30 = 5.2
"""

# main program
def main():
	try:
		check_in  = time()
		check_out = time()

		print("Please input time in hh:mm format.")
		ci = input("Check in time : ")
		co = input("Check out time: ")

		# checking input:
		if (((ci[1] != ':') and (ci[2] != ':')) or
			((co[1] != ':') and (co[2] != ':'))):
			raise format_err()


		check_in.str_to_time(ci)
		check_out.str_to_time(co)

		# check time value
		if (
			(check_out.hh <= check_in.hh) or 
			(not(check_out.hh <= 23)) or
			(not((check_in.hh == 7 and check_in.mm >= 45) or check_in.hh >= 8)) or
			(not(0 <= check_out.mm <= 59)) or
			(not(0 <= check_in.mm <= 59))
		   ):
			raise time_err()

		OT = cal_OT(check_in, check_out)

		# L is Lunch and D is Diner
		L = "N"
		D = "N"

		if (OT > 3) and (check_out.hh > 21):
			D = "Y"
		elif (OT > 4) and (  
				((check_in.hh < 12) or
				(check_in.hh == 12 and check_in.mm == 0)) and
				(check_out.hh) > 13 ):
			L = "Y"
			OT = OT - 1

		print(f"OT = {OT}, Lunch: {L}, Dinner: {D}")
		
		exit_program()
	
	except Exception as e:
		print(f"An error occurred: {e}")
		exit_program()
#end main

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()

"""OUTPUT:
Please input time in hh:mm format.
Check in time : 8:00
Check out time: 12:00
OT = 4.0, Lunch: N, Dinner: N
Exiting the program...

Please input time in hh:mm format.
Check in time : 12:00
Check out time: 16:30
OT = 3.5, Lunch: Y, Dinner: N
Exiting the program...

Please input time in hh:mm format.
Check in time : 7:00
Check out time: 9:00
An error occurred: Time value error.
Exiting the program...

Please input time in hh:mm format.
Check in time : 14:00
Check out time: 8:00
An error occurred: Time value error.
Exiting the program...

Please input time in hh:mm format.
Check in time : 7:45
Check out time: 17:45
OT = 9.0, Lunch: Y, Dinner: N
Exiting the program...

"""