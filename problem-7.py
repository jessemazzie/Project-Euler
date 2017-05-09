# Written by: Jesse Mazzie
# Problem:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def isPrime(num, count):
	for i in range(2, num):
		if num % i == 0:
			return False
	if count == 10001:
		print(num)
	return True

count, num = 0, 1

while count < 10002:
	if isPrime(num, count) is True:
		count += 1
	num += 1

#solved
	