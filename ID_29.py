unique_values = set()

for a in range(2,101):
	for b in range(2,101):
		unique_values.add(a**b)

print(len(unique_values))