def find_square_digit_chain(n):
	if n == 1 or n == 89:
		return n
	if(n in find_square_digit_chain.d):
		return find_square_digit_chain.d[n]
	s = str(n)
	summed_digits = sum([int(x)**2 for x in s])
	result = find_square_digit_chain(summed_digits)
	find_square_digit_chain.d[n] = result
	return result

find_square_digit_chain.d = {}

limit = 10000000
count_of_89 = 0


for i in range(1, limit):
	r = find_square_digit_chain(i)
	if(r == 89):
		count_of_89 += 1
		
print(count_of_89)
