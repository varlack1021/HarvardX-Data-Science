'''
Say there are three doors and one door is the correct door. 
Once a person chooses a door, one wrong door is then revealed.
The person then has two remaining doors to choose from and can either switch their choice 
and choose the other door or stay with their original door.

Question---
Is the probablity higher is they switch their choice or if the stay with their original choice?

This program does not prove mathematical only using a Monte Carlo Simulation
'''
def monty_hall_problem():

	no_change_total = 0
	change_total = 0
	limit = 10000
	
	for i in range(limit):
		doors = [0, 0, 0]
		correct = random.randrange(3)
		choice = random.randrange(3)
		doors[correct] = 1

		if doors[choice] == 1:
			no_change_total += 1
	print("Not changing choices results in a proability of {} ".format(no_change_total/limit))

	for i in range(limit):
		doors = [0, 0, 0]
		correct = random.randrange(3)
		choice = random.randrange(3)
		
		if choice == correct:		#If the person picked right then when they switch it will be incorrect
			continue			
		else:
			change_total +=1		#If person picked wrong then when they switch it will be correct

	print("Changing results in a proability of {}".format(change_total/limit))