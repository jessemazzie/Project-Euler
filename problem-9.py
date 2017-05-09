a, b, c, d = 0, 0, 0, 1000

for a in range(1, d + 1):
	for b in range(1, d + 1):
		c = a * a + b * b
		if c == d:
			print(a * b * c)
