from utils import is_prime

primes = [2]
index = 3
limit = 1000000

while index < limit:
	if is_prime(index):
		primes.append(index)		
	index += 2

max_length = 1
first_of_series = 0
for i in range(len(primes)):
	
	if i + max_length > len(primes):
		break
	max_length_from_i = max_length
	sum_from_i = sum(primes[i:i+max_length])

	for j in range(i+max_length, len(primes)):
		sum_from_i += primes[j]
		if(sum_from_i > limit):
			break
		if sum_from_i in primes:
			max_length_from_i = j-i+1

	if max_length_from_i > max_length:
		max_length = max_length_from_i
		first_of_series = i


s = sum(primes[first_of_series:first_of_series+max_length])
print(first_of_series, max_length, s)

