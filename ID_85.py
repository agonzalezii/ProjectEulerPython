def determine_number_of_recs(x,y):
	default = 0

	if x in determine_number_of_recs.hash:
		default = determine_number_of_recs.hash[x]
	else:
		default = sum(range(1,x+1))

	return sum([j * default for j in range(1,y+1)])


determine_number_of_recs.hash = {}

x = 1
goal = 2000000

#determine width
width_recs = determine_number_of_recs(x,1)
while width_recs < goal:
	x += 1
	width_recs = determine_number_of_recs(x,1)

closest = (x,1,width_recs)

print(x)
max_width = x
for y in range(1,x+1):
	for i in range(1,max_width+1):
		r = determine_number_of_recs(i,y)

		if(abs(r-goal) < abs(closest[2] - goal)):
			closest = (i,y,r)

		if r >  goal:
			max_width = i
			break

print(closest)
print(closest[0]*closest[1])
