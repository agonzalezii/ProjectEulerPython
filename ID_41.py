from itertools import permutations
from utils import is_prime

def find_pandigital_prime(n):
	for i in range(n,0,-1):
		base = ''.join([str(j) for j in range(i,0,-1)])
		perms = permutations(base)
		for p in perms:
			int_value = int(''.join(p))
			if(is_prime(int_value)):
				return int_value
		
print(find_pandigital_prime(9))
