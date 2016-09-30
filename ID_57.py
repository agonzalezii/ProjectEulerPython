from utils import digits_in_number
tries = 1000

num = 1
den = 2
#start at second iteration
numerators_over_denominators = 0
for i in range(tries):
	total_num = den + num
	
	if(digits_in_number(total_num)> digits_in_number(den)):
		numerators_over_denominators += 1

	num = den
	den += total_num
print(numerators_over_denominators)
