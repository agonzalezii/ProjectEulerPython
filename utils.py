import math

def digits_in_number(number):
	return len(str(number))

def is_palindrome(check_value):
	string_value = str(check_value)
	return string_value == string_value[::-1]

def find_prime_factorization(number, start=2):#except 1
	i = start
	primes = []

	while i <= math.sqrt(number):
		if(number % i == 0):
			primes.append(i)
			x = find_prime_factorization(number/i)
			for n in x:
				primes.append(n)
			return primes
		i +=1
	if(len(primes) == 0):
		primes.append(int(number))
	return primes

def find_divisors(number, lower_limit=1, include_self = False):
	if number < lower_limit:
		return []

	divisors = []
	index = lower_limit
	while index <= math.sqrt(number):
		division_result = number / index

		if division_result % 1 == 0 and number % division_result == 0:
			divisors.append(index)
			result_int = int(division_result)
			if(result_int != index and result_int != number):
				divisors.append(int(division_result))
		index += 1
	if(include_self):
		divisors.append(number)
	return divisors

def is_prime(number):
	if(number == 1):
		return False
	index = 2
	while index <= math.sqrt(number):
		if(number % index == 0):
			return False;
		index +=1
	return True;


def product_set(int_set):
	total = 1
	for x in int_set:
		total *= x
	return total

#triangle = n(n+1)/2
def is_triangular(number):
	inner = 8*number + 1
	s = math.sqrt(inner)
	if(s % 2 == 1):
		return True
	return False


def word_sum(word):
	name_score = 0
	for l in word:
		name_score += ord(l) - 64
	return name_score

def get_max_value(dic):
	print(max(dic, key=dic.get))

def add_or_increment(dic, v):
	if v in dic:
		dic[v] += 1
	else:
		dic[v] = 1
