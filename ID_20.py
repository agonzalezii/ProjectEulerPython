import math

x = math.factorial(100)

to_string = str(x)
total = 0

for s in to_string:
	total += int(s)


print(total)

