import math


#find limit
i = 1
limit = math.factorial(9)*i

while(i < len(str(limit))):
	i += 1
	limit = math.factorial(9)*i

digit_to_factorial = {}

#create map
for d in range(10):
	digit_to_factorial[str(d)] = math.factorial(d)

x = 3 #1 and 2 dont count
total = 0
while x <= limit:
	factorial_sum = sum([digit_to_factorial[y] for y in str(x)])
	if(factorial_sum == x):
		total += x
	x += 1

print (total)