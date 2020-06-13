import random
#0 are Reublicans
#1 are Democrats
r = [0 for x in range(125)]
d = [1 for x in range(125)]
voters = r + d

random_variable_values = []

for x in range(4):
	p = 0
	for y in range(25):
		rand = random.randrange(250)
		if voters[rand] == 1:
			p +=1
	random_variable_values.append(p)

random_variable_proportions = [p / 25 for p in random_variable_values]
print(random_variable_proportions)