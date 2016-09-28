import math
from utils import is_triangular

#triangle = n(n+1)/2
#pentagon = n(3n-1)/2
#hexagon  = n(2n-1)


def is_pentagonal(number):
	inner = 24 * number + 1
	s = math.sqrt(inner)
	if(s % 6 == 5):
		return True
	return False

def compute_hexagonal(number):
	return (number * (number*2-1))

n = 144
while True:
	hexagon = compute_hexagonal(n)
	if(is_triangular(hexagon)):
		if(is_pentagonal(hexagon)):
			break
	n += 1
print(n)
print(compute_hexagonal(n))

