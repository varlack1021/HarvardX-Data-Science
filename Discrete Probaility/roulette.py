'''
This is an example of sample modeling. Most sampling models can be simulated using an "urn"
For the example we want to find the probabiltiy of the casino making and losing money
S will be earnings for the casino

We will simulate a 1000 people drawing playing roulette as 1 simulation
After each simulation it can be seen that S changes meaning that S is a random variable
It is more useful to place S in a normal distribution to view meaningful data

In this case we want to know the probability of S being less than zero.

'''
import random
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import statistics as st
import math
import numpy as np

def roulette():
	
	a = 0 		#what we want measure against in this case zero
	red_pocket = [0 for x in range(18)]
	black_pocket = [1 for x in range(18)]
	green_pocket = [2 for x in range(2)]
	all_earnings = []
	urn = red_pocket + black_pocket + green_pocket
	
	for y in range(10000):
		earnings = 0
		
		for x in range(1000):
			draw = random.randrange(len(urn))

			if urn[draw] == 0:
				earnings -= 1
			else:
				earnings += 1
		
		all_earnings.append(earnings)

	#Hand calculations
	probability = sum(i <= a for i in all_earnings)/10000
	average = sum(all_earnings)/10000

	difference =  [ pow(i-average, 2) for i in all_earnings ]
	a = sum(difference)/10000
	standard_deviation = math.sqrt(a)
	
	#Using a library to calculate
	mean = st.mean(all_earnings)
	std = st.pstdev(all_earnings)
	print("The probability of the earnings being less than or equal to {} is {}".format(a, probability))
	print("The average is {} ".format(mean))
	print("My calculated std {} the librarys calculated std {}".format(standard_deviation, std))
	
	#--------------------Probability Distribution Chart Display
	mu = 0				#expected value which is the average of vlaues
	sigma = 3.31		#standard error of values
	
	s = np.random.normal(mu, sigma, 10000) 
	count, bins, ignored = plt.hist(s, 10, density=True, alpha=0.75)
	
	plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) *
		np.exp( - (bins - mu)**2 / (2 * sigma**2) ),  linewidth=3, color='y')
	
	plt.grid(True)
	plt.show()

	possibilities = 10000
	less_than_zero = 25

roulette()
	