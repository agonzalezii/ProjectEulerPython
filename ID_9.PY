limit = 1000

squares = {}

for i in range(1, limit):
	squares[i] = i ** 2

for a in range(1, int(limit/2)):
	b_range = int((limit-a)/2)+1
	for b in range(a+1, b_range):
		c = limit - a - b
		
		if(squares[a] + squares[b] == squares[c]):
			print(a*b*c)
