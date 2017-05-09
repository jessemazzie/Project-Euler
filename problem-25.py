def fib(n, count):
	if len(str(n)) is 1000:
		print(count)
		return n
	return fib(n-2, count + 1) + fib(n-1, count + 1)

fib(1, 1)