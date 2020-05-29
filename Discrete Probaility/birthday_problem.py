'''
What are the chances the N number of people in a room have a birthday on the same day of the year?
'''
import random
import matplotlib.pyplot as plt1
def birthday_problem(number_people):
	#----Monte Carlo Solution
	x_axis = []
	y_axis = []

	for limits in range(10, 10000, 100):
		x_axis.append(limits)
		birthdays = []
		true = 0
		for x in range(limits):
			for y in range(number_people):
				birthday = random.randrange(365)
				if birthday in birthdays:
					true += 1
					break
				birthdays.append(birthday)
			birthdays = []
		#print(true/limits)

		y_axis.append(true/limit)
	#computation
	probability = 1
	for n in range(number_people):
		probability *= (365-n)/365
		
	print("Chances for {} is {}".format(number_people, round(1-probability, 2)))

	plt.plot(x_axis, y_axis, 'ro')
	plt.show()
