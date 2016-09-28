f_1 = 1
f_2 = 1
index = 3
f_active = f_1+ f_2

desired_length = 1000

while(len(str(f_active))< desired_length):
	f_1 = f_2
	f_2 = f_active
	f_active = f_2 + f_1
	index += 1


print(index)
