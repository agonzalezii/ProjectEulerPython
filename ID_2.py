k_0 = 0
k_1 = 1
n_0 = 1
n_1 = 2
total = 0

v = 0

while True:
	v = (k_0*n_0)+(k_1*n_1)
	if(v > 4000000):
		break
	total += v
	k_1 += v+k_0
	k_0 = v


print(total)
