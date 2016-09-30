currency = [1,2,5,10,20,50,100,200]

def find_subsets(goal, coins):
	if(goal == 0):
		return 0

	subset_count = 0
	currency_declining = sorted(set(coins), reverse=True)
	for i in range(len(coins)):
		if(coins[i] > goal):
			continue
		elif(coins[i] == goal):
			subset_count += 1
		else:
			subset_count += find_subsets(goal-coins[i],coins[i:])
	return subset_count



x = find_subsets(200, currency)
print(x)