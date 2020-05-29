'''
Demonstration of finding a probability through random bag sampling
Uses the Mathematics and Monte Carlo Theorem as Proof
'''
import random
def bag_probability(**kwargs):
	limit = 10000
	sample_size = kwargs['sample_size']
	items = kwargs['items']
	bag = kwargs['bag']
	trial = {}

	#Mathematical computation
	for item in items:
		proability = item/sample_size
		trial[str(item)] = 0
		print("{}s computed proability is {}".format(item, round(proability, 2)))

	#Monte Carlo
	for i in range(limit):
		x = random.randrange(sample_size)
		result = bag[x]
		trial[str(result)]+=1
	
	print("-----Monte Carlo Probability")
	for item, total in trial.items():
		print("{}s proability is {}".format(item, total/limit ))