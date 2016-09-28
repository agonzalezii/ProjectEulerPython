from utils import *

count = 0
index = 1

while (count < 10001):
	index +=1
	if(is_prime(index)):
		print(index)
		count +=1

