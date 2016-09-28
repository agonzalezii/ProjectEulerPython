from utils import is_prime


def is_right_prime(number):
	#print("right")
	if(number == 0):
		return True
	if(is_prime(number)):
		#print(number, int(number/10))
		return is_right_prime(int(number/10))
	return False
def is_left_prime(number):
	#print("left")
	if(number == 0):
		return True
	if(is_prime(number)):
		length = len(str(number))
		power = 10 ** (length-1)
		#print(number, length, power, number % power)
		if(length == 1):
			return True
		return is_left_prime(number % power)
	return False
#[23, 29, 31, 37, 53, 59, 71, 73, 79, 233, 239]


desired_number = 11
index = 11
primes = []

while len(primes) < desired_number:
	if(is_right_prime(index)):
		if(is_left_prime(index)):
			primes.append(index)
	index += 2

print(primes)
print(sum(primes))
