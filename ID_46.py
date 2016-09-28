import math
from utils import is_prime

primes = [2]
index = 3

def conforms_to_goldbachs(number):
	if(is_prime(number)):
		primes.append(number)
		return True

	for p in primes:
		square_value = (index - p)/2
		sq_rt = math.sqrt(square_value)
		if(sq_rt == int(sq_rt)):
			#print(number, p, sq_rt)
			return True
	return False

while conforms_to_goldbachs(index):
	index += 2

print(index)
	