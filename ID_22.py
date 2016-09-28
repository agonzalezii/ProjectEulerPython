f = open('p022_names.txt', 'r');

all_names = f.readline()
all_names = all_names.replace("\"","")

names = all_names.split(',')

names.sort()

index = 0
total_score = 0

for name in names:
	index += 1
	name_score = 0
	for l in name:
		name_score += ord(l) - 64 #1 - ord('A')
	total_score += (name_score*index)
	
print(total_score)
