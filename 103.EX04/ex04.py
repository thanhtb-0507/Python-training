"""
Python practice bai 4:
author: Tran Ba Thanh
date: 18/07/2024

remaining proplem:
	- number count as str

"""

# import
import sys

# exception

# class definition
		

# function definition
def format_name(input_name):
	try:
		# delete blank space at the start and end
		cleaned_name = input_name.strip()

		# lower cased and trun into list
		words = cleaned_name.lower().split()

		wlen = len(words)
		# create output string
		formatted_name = ""
		formatted_name = words[wlen - 1].capitalize()[0] + words[wlen - 1].capitalize()[1:]
		for word in words[:(wlen - 1)]:
		    formatted_name += word.capitalize()[0]
		return formatted_name
	except Exception as e:
		raise e
	

# main program
def main():
	try:
		input_name = input("Input name: ")

		formatted_name = format_name(input_name)

		print(f"Output: {formatted_name}")

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
Input name:"    le thi  bE nHo  "
Output: NhoLTB

Input name:"    TrAn      Ba       tHanH       "
Output: ThanhTB

Input name:" nguyen mat tROi "
Output: TroiNM

Input name: ha ah ba 12
Output: 12HAB
"""