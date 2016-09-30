from utils import find_divisors

abundant_numbers = []
limit = 28124

#find all abundant numbers
for i in range(1,limit):
	divisors = find_divisors(i)
	if(sum(divisors) > i):
		abundant_numbers.append(i)

abundant_set = set(abundant_numbers)

def is_abundant_summed(arg):
	for n in abundant_numbers:
		if n > arg/2:
			return False
		if arg-n in abundant_set:
			return True
	return False



non_abundant_sum = 0
#for each number < 28123
#for each abundant number < half i
#is i - number in abundant numbers
for i in range(1, limit):
	if(not is_abundant_summed(i)):
		non_abundant_sum += i
print(non_abundant_sum)