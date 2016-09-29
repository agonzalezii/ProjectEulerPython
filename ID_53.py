import math

n = 101
limit = 1000000
n_to_fact = {}
combinations_over_limit = 0

#create dic
for i in range(n):
	n_to_fact[i] = math.factorial(i)

for i in range(n):
	halfway = int(i/2)
	for r in range(i):
		c = n_to_fact[i]/(n_to_fact[r]*n_to_fact[i-r])

		if(c > limit):
			combinations_over_limit += 1

print(combinations_over_limit)