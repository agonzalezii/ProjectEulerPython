from utils import find_divisors

index = 2
triangle_number = 1
divisors = find_divisors(triangle_number)

while(len(divisors) < 500):
	triangle_number += index
	index += 1
	divisors = find_divisors(triangle_number, include_self=True)

print(triangle_number)
#76576500