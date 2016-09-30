currency = [1,2,5,10,20,50,100,200]

def find_subsets(goal, coins):
	if(goal == 0):
		return 0

	subset_count = 0
	currency_declining = sorted(set(coins), reverse=True)
	for i in range(len(coins)):
		if(coins[i] > goal):
			continue
		elif(coins[i] == goal):
			subset_count += 1
		else:
			subset_count += find_subsets(goal-coins[i],coins[i:])
	return subset_count



x = find_subsets(200, currency)
print(x)














































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

