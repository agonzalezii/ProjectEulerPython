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
























'''
Problem 549 -> need to switch to sieve and test method here against size

from math import *
from utils import find_prime_factorization

def factorial_with_prime_factorization(number, count):
	index = 0
	while count > 0:
		index += 1
		count -= 1 
		x = index
		while(x> 0 and x % number == 0):
			count -= 1
			x/=number
	return number * index

pf = find_prime_factorization(10)
c = [(i, pf.count(i)) for i in set(pf)]

limit = (10**5)
index = 1
S_N = 0

while index < limit:
	index += 1
	#print(("i",index))
	p_f = find_prime_factorization(index)
	#print(p_f)
	
	
	counts = [(i, p_f.count(i)) for i in set(p_f)]
	#print(counts)
	s_index = max([factorial_with_prime_factorization(i,j) for i,j in counts])
	S_N += s_index
	#print(("s",s_index))
print(S_N)

'''

