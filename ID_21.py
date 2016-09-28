from utils import *

limit = 10000

index = 1
number_to_divisors = {}
number_to_divisor_sum = {}
amicable_numbers = []


while index <= limit:
	divisors = find_divisors(index)
	number_to_divisors[index] = divisors
	number_to_divisor_sum[index] = sum(divisors)
	index += 1

for number in number_to_divisor_sum:
	potential_amicable_pair = number_to_divisor_sum[number]
	if potential_amicable_pair not in number_to_divisor_sum:
		continue

	potential_pairs_pair = number_to_divisor_sum[potential_amicable_pair]

	if(number == potential_amicable_pair):
		continue


	if potential_pairs_pair == number:
		amicable_numbers.append(number)

print(sum(amicable_numbers))


