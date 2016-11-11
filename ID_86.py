# problem 86 https://cat100percentile.com/2013/09/26/shortest-path-cuboid/
squares = set()

solutions = 0
solution_goal = 1000000

a = 0
squares_index = 1
calc_square = 1

while solutions < solution_goal:
	a += 1	
	a_squared = a ** 2

	#generate accepted squares
	squares_limit = a_squared * 5
	while calc_square <= squares_limit:
		squares.add(calc_square)
		squares_index += 1
		calc_square = squares_index ** 2
		

	# are squares available in b+c
	for s in squares:
		v = s - a_squared
		if v in squares:
			
			sq_v = v**(1/2)
			if(a < sq_v):
				thishere = int((a - (sq_v - a))/2)+1
				solutions += thishere
			else:
				solutions += int(sq_v/2)


print(a)