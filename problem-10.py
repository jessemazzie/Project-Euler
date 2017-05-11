import math

def isPrime(num):
	if num <= 1:
		return False
	elif num is 2:
		return True
	elif num % 2 is 0:
		return False
	else:
		for i in range(2, int(math.sqrt(num)) + 1):
			if num % i == 0:
				return False
		return True


sum = 0

for i in range(2, 2000000):
	if isPrime(i):
		sum += i


print(sum)
