# Written by: Jesse Mazzie
# Problem:
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquare():
	sum = 0
	for i in range(1, 101):
		sum += i * i
	return sum
def squareOfSum():
	sum = 0
	for i in range(1, 101):
		sum += i
	print(sum)
	return (sum * sum)

difference = (sumOfSquare() - squareOfSum())
print(difference)

#solved