from utils import is_prime
primes = set()

for i in range(1000,10000):
	if(is_prime(i)):
		primes.add(i)

dic = {}
for p in primes:
	s = ''.join(sorted(str(p)))
	if s in dic:
		dic[s].append(p)
	else:
		dic[s] = [p]

for kvp in dic:
	v = dic[kvp]
	l = len(v)
	if(l < 3):
		i += 1
		continue
	v.sort()
	for i in range(l-2):
		for j in range(i+1, l-1):
			diff = v[j] - v[i]
			if(v[j] + diff in v):
				print(v[i],v[j],v[j]+diff)
				print(v)


print(len(dic))
