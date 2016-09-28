from utils import is_palindrome

i = 1
j = 1

limit = 1000

max_value = 0

while i < limit:
	while j< limit:
		total = i * j
		if(is_palindrome(total)):
			max_value = max(max_value, total)
		j += 1
	
	i+=1
	j = 1

print(max_value)
