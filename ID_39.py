import math

n = 1
p_limit = 1000
p_to_count = {}

while n < p_limit:
	m = n+1
	while m < p_limit:
		c = math.sqrt(n**2 + m**2)
		perimeter = n+m+c
		m+=1
		if(int(c) != c):
			continue
		
		if(perimeter > p_limit):
			continue

		if(perimeter in p_to_count):
			p_to_count[perimeter] += 1
		else:
			p_to_count[perimeter] = 1
		
	n+=1
print(max(p_to_count, key=p_to_count.get))



