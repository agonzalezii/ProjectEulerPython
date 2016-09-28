total_sum = 0;

# max of any digit is 9**5 = 59049; find n where 59049*n < 10**n; n=6 so thats the max number of places

for i in range(10):
	for j in range(10):
		for k in range(10):
			for l in range(10):
				for m in range(10):
					for n in range(10):
						power_sum = (i**5)+(j**5)+(k**5)+(l**5)+(m**5)+(n**5);
						expected_value = i + (10*j) + (100*k) + (1000*l) + (10000*m) + (100000*n)
						if(power_sum == expected_value):
							total_sum += expected_value
							print(n, m,l,k,j,i)
							print(expected_value)

print(total_sum - 1) # 1 is not a sum

