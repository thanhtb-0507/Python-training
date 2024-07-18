"""
Python practice bai 5:
author: Tran Ba Thanh
date: 18/07/2024

remaining proplem:
	- 

"""

# import
import sys

# exception

# class definition
		

# function definition
def count_elements(lst):
	""" docstring for count_elements """
	count_dict = {}
	for item in lst:
		if item in count_dict:
			count_dict[item] += 1
		else:
			count_dict[item] = 1
	return count_dict

def sort_dict_by_value(d):
	""" docstring for sort_dict_by_value """
	return {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}
	

# main program
def main():
	try:
		# input N, number of elements in the list
		N = int(input("N = "))

		# input list's elements
		elements = []
		print("Input elements:")
		for i in range(N):
			element = int(input(f"n{i} = "))
			elements.append(element)

		count_dict = count_elements(elements)
		sorted_dict = sort_dict_by_value(count_dict)

		print("Sorted and count dict:")
		print(sorted_dict)

	except ValueError:
		print("Please input integer.")
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

try 1:
	N = 10
	Input elements:
	n0 = 1
	n1 = 2
	n2 = 3
	n3 = 3
	n4 = 3
	n5 = 3
	n6 = 3
	n7 = 3
	n8 = 3
	n9 = 3
	Sorted and count dict:
	{1: 1, 2: 1, 3: 8}
	
try 2:
	N = 10
	Input elements:
	n0 = 1
	n1 = 2
	n2 = 4
	n3 = 5
	n4 = 2
	n5 = 4
	n6 = 1
	n7 = 6
	n8 = 4
	n9 = 3
	Sorted and count dict:
	{5: 1, 6: 1, 3: 1, 1: 2, 2: 2, 4: 3}
"""