"""
File: quadratic_solver.py
Name: Michelle Lan
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	quadratic solver
	"""
	print("stanCode Quadratic Solver!")
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	c = int(input("Enter c: "))

	y = b*b - 4*a*c

	# prevent from math domain error
	if y < 0:
		print('No real roots')
	else:
		f = math.sqrt(y)
		if y == 0:
			print('One root: ' + str((f - b)/(2*a)))
		elif y > 0:
			print('Two roots: ' + str((f - b)/(2*a)) + ' , ' + str((f + b)*(-1)/(2*a)))


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
