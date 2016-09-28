
total_sum = 1
side_length = 3

side_lenth_goal = 1001

while side_length <= side_lenth_goal:
	total_sum += (4*(side_length**2)-(6*side_length)+6)
	side_length += 2

print(total_sum)
