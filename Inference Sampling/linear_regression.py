'''
This is code is my documentation of my first time using
the pandas module.
I demonstrate how we mathematically (using module functions)
use correlation to get to regression
'''
import csv
import random
import requests
import numpy as np
import pandas as pd
from pprint import pprint
from scipy.stats import linregress
import statistics as st
import matplotlib.pyplot as plt 

galon_heights_url = "http://www.randomservices.org/random/data/Galton.txt" 
session = requests.Session()

response = session.get(galon_heights_url)
decoded_content = response.content.decode('ISO-8859-1')

#--------Initializing Data Frame------------------------
data_iter = csv.reader(decoded_content.splitlines(), delimiter='\t')
data = [data for data in data_iter]

df = pd.DataFrame(data[1:])
df.columns = data[0]

#-------Accessing Attributes---------------------------
#print("Head----")
#print(df.head())
#print(df.dtypes)


#get attributes of the df
#.types, index, columns, values

#statistrical summary of each column
#print(df.describe())

#-----------Converting column data types---------------
#Right now there are just labelled as 'objects'
#There are mutltiple ways to do this

#Option 1
convert_list = ['Father', 'Height', ]
df[convert_list] = df[convert_list].apply(pd.to_numeric)

#Option2
convert_dic = {'Father': float, 
				'Height': float,
				}
df = df.astype(convert_dic)

#-----Access a rows and columns of data------

#rows, columns
#loc is used for categorical data
#iloc is for indexing data
x = df.loc[ 0: 25, ['Father', 'Height'] ]


#----Removing Data------
#Removing all rows with gender F
#Need to set index to the column we want to remove data first
#This removed the column of indexes though
df = df.set_index('Gender')

df = df.drop('F')
#sets index back to default one
#default labels each row one by one
df = df.reset_index()

#----Remove Duplice Data-----
#For this particular data set I only want 1 father and 1 son

df.drop_duplicates(subset='Family',  inplace=True)
df = df.reset_index()

#------Rename Column
df = df.rename({'Height': 'Son'}, axis='columns')

#---Correlation Between Two Columns
correlation = df['Father'].corr(df['Son'])
print("Correlation between Father and Son is {}".format(correlation))

#--Sampling Correlation is a Random Variable--------

sample_size = 25
random_variable = []

for i in range(1000):
	sample = df.sample(sample_size)
	correlation = sample['Father'].corr(sample['Son'])
	random_variable.append(correlation)

mu = st.mean(random_variable)
sigma = st.pstdev(random_variable)

#---Plotting Histogram---------
s = np.random.normal(mu, sigma, 10000) 
count, bins, ignored = plt.hist(s, 10, density=True, alpha=0.75)

#plt.plot(bins, 1/(sigma * np.sqrt(2*np.pi)) *
#	np.exp( - (bins - mu)**2 / (2 * sigma**2) ),  linewidth=3, color='y')

#plt.grid(True)
#plt.show()

#-----Round a Column--------
df = df.round()

#---Count values in the column
#print(df['Father'].value_counts())

#-----Box Plot--------------
boxplot = df.boxplot(by='Father', column='Son')

#---Conditional Average-----
conditional_mean = df.groupby('Father').mean()
conditional_mean = conditional_mean.rename({'Son': 'Son_Conditional_Average'}, axis='columns')
conditional_mean = conditional_mean.reset_index()

#---Join Column from anothe DF
df = df.join(conditional_mean['Son_Conditional_Average'])

#---Sactter Plot------------
ax = conditional_mean.plot.scatter(x='Father', y='Son_Conditional_Average')

#---Line of best fit--------
#Here I am using pyplot. Did not find it in pandas
#Pandas also did not offer a way to find the slope
#Manually calculate it or use scipy module

x = df['Son']
y = df['Father']
plt.plot(x, y, 'o')

m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b)

plot_info = linregress(x, y)
print(plot_info)

plt.show()







