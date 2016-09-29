from utils import add_or_increment
def same_digits(a, b):
	digits_of_a = {}
	digits_of_b = {}
	s_a = str(a)
	s_b = str(b)
	if(len(s_a) != len(s_b)):
		return False
	for c in s_a:
		add_or_increment(digits_of_a, c)
	for c in s_b:
		add_or_increment(digits_of_b, c)
	if(len(digits_of_a) != len(digits_of_b)):
		return False
	for k_a in digits_of_a:
		if k_a not in digits_of_b:
			return False
		if digits_of_a[k_a] != digits_of_b[k_a]:
			return False
	return True


def all_same_to_n(a,n):
	for i in range(1,n):
		if(not same_digits(a, a * (i+1))):
			return False
	return True


print(all_same_to_n(125874, 2))

i = 2
n = 6
not_found = True

while not all_same_to_n(i,n):
	i += 1

print(i)
