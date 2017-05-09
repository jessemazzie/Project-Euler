# Written by: Jesse Mazzie
# Problem:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def isPalindrome(pp):
	if str(pp) == str(pp)[::-1]:
		return int(pp)
	else:
		return 0

highest = 0

for i in range(1, 1000):
	for j in range(1, 1000):
		palindrome = isPalindrome(i * j)
		if palindrome > highest:
			highest = palindrome

print(highest)

#solved