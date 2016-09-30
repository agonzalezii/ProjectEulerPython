from utils import digits_in_number


def is_unique(s):
	unique_chars = set([c for c in s])
	return len(s) == len(unique_chars)

def is_three_digit_unique(number):
	s = str(number)
	if(len(s)) > 3:
		return False
	if(len(s) < 3):
		s = "0"*(3-len(s))+s
	return is_unique(s)

three_unique = set()
for i in range(1000):
	if(is_three_digit_unique(i)):
		three_unique.add(i)

divisible_by_2 = [x for x in three_unique if x%2==0]
divisible_by_3 = set([x for x in three_unique if x%3==0])
divisible_by_5 = set([x for x in three_unique if x%5==0])
divisible_by_7 = [x for x in three_unique if x%7==0]
divisible_by_11 = set([x for x in three_unique if x%11==0])
divisible_by_13 = set([x for x in three_unique if x%13==0])
divisible_by_17 = [x for x in three_unique if x%17==0]

print(len(divisible_by_17),len(divisible_by_7),len(divisible_by_2))
complete_numbers = []
for d2 in divisible_by_2:
	for d7 in divisible_by_7:
		for d17 in divisible_by_17:
			s = str(d2) + str(d7)+str(d17)
			if is_unique(s):
				complete_numbers.append(s)

divisible_numbers = []
for cn in complete_numbers:
	if int(cn[1:4]) not in divisible_by_3:
		continue
	if int(cn[2:5]) not in divisible_by_5:
		continue
	if int(cn[4:7]) not in divisible_by_11:
		continue
	if int(cn[5:8]) not in divisible_by_13:
		continue
	divisible_numbers.append(cn)

first_digit = [i for i in range(10)]
total = 0
for dn in divisible_numbers:
	for c in first_digit:
		if str(c) not in dn:
			total += int(str(c)+dn)

print(total)