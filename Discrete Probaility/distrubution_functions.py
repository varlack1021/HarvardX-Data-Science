import scipy.stats as st
import math
import numpy as np
import matplotlib.pyplot as plt
import math

#what is the minimum p where the score is 35 or higher 80% of the time?
def prbablity_distribution(p, a):
	mu = 44 *p
	sigma = math.sqrt(44) * abs(1-0) * math.sqrt(p*(1-p))
	
	return ( 0.5 * (1 + math.erf((a - mu)/math.sqrt(2 * sigma**2))))

def display_normal_distrubution(p, a):
	mu = 44 *p
	sigma = math.sqrt(44) * abs(1-0) * math.sqrt(p*(1-p))
	
	s = np.random.normal(mu, sigma, 10000) 
	count, bins, ignored = plt.hist(s, 10, density=True, alpha=0.75)
	
	plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) *
		np.exp( - (bins - mu)**2 / (2 * sigma**2) ),  linewidth=3, color='y')
	
	plt.grid(True)
	plt.show()

def find_min_p_for_a(a, interval, *args):
	p = .01
	while(True):
		result = prbablity_distribution(p, a)
		if result < interval:
			break
		p += .01
		p = round(p, 2)

	if args:
		display_normal_distrubution(p, a)

	return p 
	
p = find_min_p_for_a(35, .2, True)
print("p is ", p)
