

# problem 86 https://cat100percentile.com/2013/09/26/shortest-path-cuboid/
squares = set()

solutions = 0
solution_goal = 1000000

a = 0
squares_index = 1
calc_square = 1

while solutions < solution_goal:
	a += 1	
	a_squared = a ** 2

	#generate accepted squares
	squares_limit = a_squared * 5
	while calc_square <= squares_limit:
		squares.add(calc_square)
		squares_index += 1
		calc_square = squares_index ** 2
		

	# are squares available in b+c
	for s in squares:
		v = s - a_squared
		if v in squares:
			
			sq_v = v**(1/2)
			if(a < sq_v):
				thishere = int((a - (sq_v - a))/2)+1
				solutions += thishere
			else:
				solutions += int(sq_v/2)


print(a)
		













































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

