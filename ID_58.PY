from utils import is_prime
primes = []

side_length = 3
min_length = 8
total = 1
prime_limit = .1


while len(primes)/total > prime_limit or side_length < min_length :
	corner_rd = side_length ** 2
	corners = [corner_rd - (i*(side_length-1)) for i in range(4)]
	for corner in corners:
		if(is_prime(corner)):
			primes.append(corner)
	side_length += 2
	total += 4

print(side_length-2)
