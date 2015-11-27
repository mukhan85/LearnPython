import sys

file = open('hackerInput', 'r')


def solve(number):
    counter = 0
    original_number = int(number)
    for each_digit in str(number):
        int_digit = int(each_digit)
        if int_digit != 0 and original_number % int_digit == 0:
            counter += 1
    print(counter)

t = int(file.readline())

for a0 in range(t):
    n = int(file.readline())
    solve(n)

file.close()
