"""
File: weather_master.py
Name: Michelle Lan
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This number controls when to stop the function
EXIT = -100


def main():
	"""
	weather master
	"""
	print("stanCode \"Weather Master 4.0\"!")
	f = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	total = 0
	# total temperatures user input
	high = f
	# highest temperature
	low = f
	# lowest temperature
	cold = 0
	# how many days the temperature < 16
	days = 0
	# how many days

	if f == EXIT:
		print('No temperatures were entered.')
	else:
		while True:
			if f == EXIT:
				break
			elif f > high:
				high = f
			elif f < low:
				low = f

			if f < 16:
				cold += 1

			total += f
			days += 1
			f = int(input('Next Temperature: (or ' + str(EXIT) + 'to quit)? '))

		average = total/days
		# average temperatures

		print('Highest temperature = ' + str(high))
		print('Lowest temperature = ' + str(low))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
