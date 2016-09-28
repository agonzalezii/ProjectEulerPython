from utils import *

total_sum = 0
index = 1
upper_bound = 1000000

while index < upper_bound:
	if(is_palindrome(index)):
		result = is_palindrome(str(bin(index))[2:])
		if(result):
			total_sum += index
	index += 1
print(total_sum)