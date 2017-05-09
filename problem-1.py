# Written by: Jesse Mazzie
# Problem:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


sum = 0
max = 1000
count = 0

for count in range(0, max):
	if count % 3 is 0 or count % 5 is 0:
		sum += count
		count += 1
	else:
		count += 1

print(sum)

#solved
