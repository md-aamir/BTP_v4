##################################################Extract Output from Output file##########################################################
n_samples=50#0-49
n_pow=81#0-80

file1 = open("POWER","r+")
Out=file1.read().split()
	
# Number of rows = 50 (ie, number of Samples), each column belongs to a different Samples]
# so, all the rows of a column is my Sample space
CLASS0=[]
CLASS1=[]
i=0
for i in range(n_samples):
	s="CLASS0_SAMPLE"+str(i)
	m=Out.index(s)
	Out=Out[m+1:]
	tem=[]
	for x in range(n_pow):
		s="*POW"+str(x)
		m=Out.index(s)
		tem.append(Out[m+2])
	CLASS0.append(tem)

	s="CLASS1_SAMPLE"+str(i)
	Out=Out[m+1:]
	m=Out.index(s)
	Out=Out[m+1:]
	tem=[]
	for x in range(n_pow):
		s="*POW"+str(x)
		m=Out.index(s)
		tem.append(Out[m+2])
	CLASS1.append(tem)
Samples_c0=[]
Samples_c1=[]
for x in range(len(CLASS0[0])):
	temp0=[]
	temp1=[]
	for i in range(len(CLASS0)):
		temp0.append(CLASS0[i][x])
		temp1.append(CLASS1[i][x])
	Samples_c0.append(temp0)
	Samples_c1.append(temp1)
#########################################################
import statistics
import scipy.stats
mean0=[]
mean1=[]
stdev0=[]
stdev1=[]
for x in range(len(CLASS0[0])):
	a=[]
	b=[]
	for y in range(len(CLASS0)):
		a.append(float(CLASS0[y][x]))
		b.append(float(CLASS1[y][x]))

	mean0.append(statistics.mean(a))
	stdev0.append(statistics.stdev(a,statistics.mean(a)))
	mean1.append(statistics.mean(b))
	stdev1.append(statistics.stdev(b,statistics.mean(b)))

ttest=[]	
for x in range(len(mean1)):
	a=[]
	Z=scipy.stats.ttest_ind_from_stats(mean1[x], stdev1[x],50, mean0[x], stdev0[x], 50, equal_var=False)
	a.append(float(Z[0]))
	a.append(float(Z[1]))
	ttest.append(a)

print(scipy.stats.ttest_ind_from_stats(mean1[0], stdev1[0],50, mean1[0], stdev1[0], 50, equal_var=False))


from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(10,45,0.1)
sigma = 2
print('Mean :', round(x.mean(), 2),'SD :', sigma)
plt.plot(x, norm.pdf(x,x.mean(),sigma), 'r1', lw=2, alpha=0.5, label='norm PDF')
plt.legend(loc='best')
plt.show()