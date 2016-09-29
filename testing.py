from utils import add_or_increment
def same_digits(a, b):
	digits_of_a = {}
	digits_of_b = {}
	s_a = str(a)
	s_b = str(b)
	if(len(s_a) != len(s_b)):
		return False
	for c in s_a:
		add_or_increment(digits_of_a, c)
	for c in s_b:
		add_or_increment(digits_of_b, c)
	if(len(digits_of_a) != len(digits_of_b)):
		return False
	for k_a in digits_of_a:
		if k_a not in digits_of_b:
			return False
		if digits_of_a[k_a] != digits_of_b[k_a]:
			return False
	return True


def all_same_to_n(a,n):
	for i in range(1,n):
		if(not same_digits(a, a * (i+1))):
			return False
	return True


print(all_same_to_n(125874, 2))

limit = 1000000
n = 6
not_found = True

for i in range(1,limit):
	if(all_same_to_n(i, n)):
		print(i)































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

