from utils import is_prime

overall_limit = 50000000

square_root_limit = int(overall_limit**(1/2))
cube_root_limit = int(overall_limit**(1/3))
fourth_root_limit = int(overall_limit**(1/4))

print(square_root_limit)
print(cube_root_limit)
print(fourth_root_limit)

squares = []
cubes = []
fourths = []
for i in range(2, square_root_limit+1):
	if(is_prime(i)):
		square = i**2
		squares.append(square)
		if(i< cube_root_limit):
			cubes.append(square * i)
		if(i< fourth_root_limit):
			fourths.append(square * square)

values = set()
for s in squares:
	for c in cubes:
		for f in fourths:
			v = s+c+f
			if v > overall_limit:
				break
			values.add(v)

print(len(values))