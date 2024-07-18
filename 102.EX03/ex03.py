"""
Python practice bai 3:
author: Tran Ba Thanh
date: 18/07/2024

remaining proplem:
	- 

"""

# import
import sys
import datetime

# exception
class DateError(Exception):
	"""docstring for DateError"""
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)



# class definition

		

# function definition
def convert_str_to_date(date_str):
    """Convert a string in dd/mm/yyyy format to a datetime object."""
    try:
        date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
        return date_obj
    except ValueError:
        raise DateError("Invalid date format, must be dd/mm/yyyy!")

def check_date_validity(date_obj):
    """Check if the date is valid and falls within a reasonable range."""
    today = datetime.datetime.today()
    if date_obj > today:
        raise DateError("The date cannot be in the future.")
    elif date_obj.year < 1900:
        raise DateError("Are you a zombie?")

def cal_leave_days(join_date):
	"""Calculate the number of leave days."""
	today = datetime.datetime.today()
	years_of_service = today.year - join_date.year
	if join_date > today.replace(year=join_date.year):
		years_of_service -= 1

	if years_of_service >= 5:
		return 14.0
	elif years_of_service >= 4:
		return 13.0
	elif years_of_service >= 1:
		return 12.0
	else:
		# Calculate leave days for current year joiners
		leave_days = 0.0
		remaining_months = 12 - join_date.month
		if join_date.day >= 10:
			leave_days += 0.5 + (remaining_months * 1)
		else:
			leave_days += 1 + (remaining_months * 1)
		return leave_days

# main program
def main():
	try:
		print("Please input in dd/mm/yyyy format.")
		input_date = convert_str_to_date(input("Date: "))
		check_date_validity(input_date)

		leave_days = cal_leave_days(input_date)

		print(	f"Ngay vao lam: {input_date.strftime('%d/%m/%Y')} : "
				f"So ngay nghi phep: {leave_days}")

	except DateError as e:
		print(f"An error occurred: {e.message}")
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

Date: 10/3/2020
Ngay vao lam: 10/03/2020 : So ngay nghi phep: 13.0


Date: 4/12/2019
Ngay vao lam: 04/12/2019 : So ngay nghi phep: 13.0


Date: 1/3/2019
Ngay vao lam: 01/03/2019 : So ngay nghi phep: 14.0


Date: 1/2/2024
Ngay vao lam: 01/02/2024 : So ngay nghi phep: 11.0

Date: 0/1
An error occurred: Invalid date format, must be dd/mm/yyyy!

Date: 10/10/2024
An error occurred: The date cannot be in the future.

Date: 1/9/1899
An error occurred: Are you a zombie?

"""