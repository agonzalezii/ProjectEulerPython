from utils import find_prime_factorization

working_set = []
desired_unique = 4
for i in range(desired_unique):
	working_set.append(i+1)


def check_for_primeness(numbers):
	prime_factors = set()
	for i in numbers:
		primes = set(find_prime_factorization(i))
		if(len(primes) < desired_unique):
			return False
	return True



while not check_for_primeness(working_set):
	i = working_set.pop(0)
	working_set.append(i + desired_unique)
	

print(working_set)



