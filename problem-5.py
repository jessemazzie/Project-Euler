# Written by: Jesse Mazzie
# Problem:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


check_list = [11, 13, 14, 16, 17, 18, 19, 20]

for num in range(20, 999999999, 20):
	if all(num % n == 0 for n in check_list):
		print(num)
		break

#solved