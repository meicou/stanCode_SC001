"""
File: hailstone.py
Name: Michelle Lan
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences.
    """
    print('This program computes Hailstone sequences.\n')
    n = int(input('Enter a number: '))
    steps = 0
    data = 0

    while n != 1:
        if n == 1:
            print('It took ' + str(steps) + 'steps to teach 1.')
            break

        elif n % 2 == 1:
            data = 3*n + 1
            print(str(n) + ' is odd, so I make 3n+1: ' + str(data))

        elif n % 2 == 0:
            data = n // 2
            print(str(n) + ' is even, so I take half: ' + str(data))

        n = data
        steps += 1

    print('It took ' + str(steps) + ' steps to teach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
