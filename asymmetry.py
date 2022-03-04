import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from scores import *

sex = 'M'
lifts = {"Squat":200, "Bench":130, "Deadlift":240} #Kilograms
bw = 107. #Kilograms
open_powerlifting_csv_file = 'openpowerlifting-2021-07-28-d47e7220.csv' #Download this from openpowerlifting, use imperial system

wilks_range = 0.2 

my_total = sum([v for v in lifts.values()])
my_wilks = wilks_coeff(bw)*my_total
p = pd.read_csv('openpowerlifting-2021-07-28-d47e7220.csv')
p = p[(p['Sex'] == sex) & (p['Equipment'] == 'Raw') & (p['Best3SquatKg'] > 0) & (p['Best3BenchKg'] > 0) & (p['Best3DeadliftKg'] > 0)]
p = p[ (p['Wilks'] < my_wilks*(1+wilks_range)) & (p['Wilks'] > my_wilks*(1-wilks_range)) ]

totals = np.sum([p['Best3{:s}Kg'.format(lift)] for lift in lifts.keys()], axis = 0)
ratio_dist = {k:p['Best3{:s}Kg'.format(k)]/totals for k in lifts.keys()}
my_ratios = {k:v/my_total for k,v in lifts.items()}
z_scores = {lift:(my_ratios[lift] - np.mean(ratio_dist[lift]))/np.std(ratio_dist[lift]) for lift in lifts.keys()}

plt.title("For {:s} lifters with {:.0f} to {:.0f} Wilks scores".format("male" if sex == 'M' else "female", my_wilks*(1-wilks_range), my_wilks*(1+wilks_range)))
for c, [lift, weight] in zip(sns.color_palette("husl", len(lifts)), lifts.items()):
	plt.hist(ratio_dist[lift], bins = 150, alpha = 0.5, label = lift, color=c, density = True)
	plt.axvline(my_ratios[lift], c=c)
plt.xlabel("Fraction of total")

for lift, z_score in z_scores.items():
	print("{:s} Z-score = {:.2f}".format(lift, z_score))

plt.legend()
plt.show()


