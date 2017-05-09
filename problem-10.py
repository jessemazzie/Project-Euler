def isPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True


sum = 0

for i in range(2, 2000000):
	if isPrime(i):
		sum += i


print(sum)
