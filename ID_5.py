from utils import *

size = 20
overall_factors = {}

for i in range(size):
	i_factors = find_prime_factorization(i)
	local_map = {}
	for f in i_factors:
		if f in local_map:
			local_map[f] +=1
		else:
			local_map[f] = 1

	for f in local_map:
		if f in overall_factors:
			overall_factors[f] = max(overall_factors[f], local_map[f])
		else:
			overall_factors[f] = local_map[f]

mult =[x ** overall_factors[x] for x in overall_factors] 

total = product_set(mult)

 # 232792560
print (total)

