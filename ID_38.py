from utils import *

limit = 9876


def generate_pandigital(i):
	n = 1
	v = ""
	v_prime = str(n*i)
	
	while (is_unique(v+v_prime)):
		n += 1
		v += v_prime
		v_prime = str(n*i)
	
	if(is_pandigital(v, 1, 9)):
		return v
	return None


max_pandigital = 0
for i in range(1,limit):
	x = generate_pandigital(i)
	if(x):
		max_pandigital = max(max_pandigital, int(x))


print(max_pandigital)