from utils import is_prime

primality = {}

def local_check_prime(number):
	if(number in primality):
		return primality[number]
	number_is_prime = is_prime(number)
	primality[number] = number_is_prime
	return number_is_prime

limit = 1000
max_consecutive = 0
a_and_b = (1,1)

for a in range(-limit+1,limit):
	for b in range(-limit,limit+1,2):
		n = 0
		check = (n**2) + (a*n) + b
		while check > 0:
			if(not local_check_prime(check)):
				break
			n += 1
			check = (n**2) + (a*n) + b

		if n > max_consecutive:
			max_consecutive = n
			a_and_b = (a,b)
print(max_consecutive)
print(a_and_b)
print(a_and_b[0] * a_and_b[1])

