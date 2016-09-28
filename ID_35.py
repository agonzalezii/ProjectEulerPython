from utils import *


def rotate(number, num_of_rotations=1):
	magnitude = len(str(number))
	rotated = number % (10**num_of_rotations)
	number = ((rotated * (10**magnitude)) + number - rotated) / (10**num_of_rotations)
	return int(number)


upper_limit = 1000000
#upper_limit = 100

i = 3
circular_primes = set()

while i < upper_limit:
	if(is_prime(i)):
		mag = digits_in_number(i)
		rotation_good = True
		rotations = [rotate(i, x+1) for x in range(mag-1)]
		for rotation in rotations:
			if(rotation in circular_primes):
				continue
			if(not is_prime(rotation)):
				rotation_good = False
				break
		if(rotation_good):
			circular_primes.add(i)
			for r in rotations:
				circular_primes.add(r)
	i += 2 #skip evens

print(len(circular_primes )+ 1)# 1 for 2
