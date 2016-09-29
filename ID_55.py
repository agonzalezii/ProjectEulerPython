from utils import is_palindrome

limit = 10000
try_limit = 50
i = 1

def get_reverse(number):
	return int(str(number)[::-1])

def is_lychrel(number):
	tries = 0
	active = number
	while tries< try_limit:
		active_reverse = get_reverse(active)
		sum_with_reverse = active_reverse + active
		if(is_palindrome(sum_with_reverse)):
			return False
		tries += 1
		active = sum_with_reverse
	return True

print(sum([is_lychrel(i) for i in range(limit)]))

