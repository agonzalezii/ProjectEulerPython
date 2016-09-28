from utils import *

total_sum = 0
index = 1

while (index < 2000000):
	index +=1
	if(is_prime(index)):
		total_sum += index
print (total_sum)
