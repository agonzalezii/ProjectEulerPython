limit = 1000000

known_collatz = {1:1}

def find_collatz_sequence(number):
	count = 0

	while number not in known_collatz:
		if(number %2 == 0):
			number = number/2
		else:
			number = number*3 +1
		count +=1
	return count + known_collatz[number]

max_collatz_len = 0
max_collatz_seed = 0

for i in range(1,limit):
	collatz_length = find_collatz_sequence(i)
	known_collatz[i] = collatz_length
	if(collatz_length > max_collatz_len):
		max_collatz_seed = i
		max_collatz_len = collatz_length

print(max_collatz_seed, max_collatz_len)

