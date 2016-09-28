from utils import find_prime_factorization
fractions = []

for num in range(10, 100):
	for den in range(num, 100):
		num_tens = int(num/10)
		num_ones = num % 10

		den_tens = int(den/10)
		den_ones = den % 10

		if(den_ones == 0):
			continue
		if(num_ones != den_tens):
			continue
		if(num_ones == den_ones):
			continue

		if(num/den == num_tens/den_ones):
			fractions.append((num, den))

#find product of fractions in lowest common terms
new_num = 1
new_den = 1

for n,d in fractions:
	new_num *= n
	new_den *= d

num_prime_factorization = find_prime_factorization(new_num)
den_prime_factorization = find_prime_factorization(new_den)

to_remove = []

for i in num_prime_factorization:
	if i in den_prime_factorization:
		den_prime_factorization.remove(i)
		to_remove.append(i)
for i in to_remove:
	num_prime_factorization.remove(i)

n = 1
for i in num_prime_factorization:
	n *= i
d = 1
for i in den_prime_factorization:
	d*=i

print(n,d)