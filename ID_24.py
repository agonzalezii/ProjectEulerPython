import math
from utils import add_or_increment

available_set = [0,1,2,3,4,5,6,7,8,9]

def find_npr(n_set, r):
	unique_set = {}
	for s in n_set:
		add_or_increment(unique_set, s)
	n = len(n_set)
	p = math.factorial(n)/math.factorial(n-r)
	for key in unique_set:
		p /=  math.factorial(unique_set[key])
	return p

def find_nth_lexicographic_permutation(s, n):
	if(len(s) == 0):
		return ""

	s.sort()
	permutations_seen = 0
	for i in range(len(s)):
		subset = s[:i] + s[i+1:]
		npr = find_npr(subset, len(subset))
		#print (i, subset, npr, permutations_seen)
		if permutations_seen + npr >= n:
			return str(s[i]) + find_nth_lexicographic_permutation(subset, n-permutations_seen)
		permutations_seen += npr



	raise Exception("out of range")

ans = find_nth_lexicographic_permutation(available_set, 1000000)
print(ans)