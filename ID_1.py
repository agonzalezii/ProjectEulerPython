#sum up all numbers in range(1000) that are divisible by either 3 or 5.
i = 1
total = 0
while i< 1000:
	if(i%5 == 0 or i%3 == 0):
		total += i
	i += 1
print (total)
