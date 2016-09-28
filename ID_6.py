limit = 100
i = 1

total = 0
square_sum = 0


while i<= limit:
	total += i
	square_sum += i**2
	i += 1

total = total ** 2; 

print(total - square_sum)


