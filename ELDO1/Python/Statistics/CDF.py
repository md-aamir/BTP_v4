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
		temp0.append(float(CLASS0[i][x]))
		temp1.append(float(CLASS1[i][x]))
	Samples_c0.append(temp0)
	Samples_c1.append(temp1)
#########################################################
# import matplotlib.pyplot as plt
from matplotlib import pyplot
for i in range(len(Samples_c0)):
	Samples_c0[i].sort()
	Samples_c1[i].sort()

#Number of Data Points:
num_datapoints=len(Samples_c0[0])


#probability that this point is at or below in our data point
actual_freq=[]
x=1/num_datapoints
y=0
for i in range(len(Samples_c0[0])):
	y=y+x
	actual_freq.append(y)
# plt.plot(Samples_c0[0],actual_freq,color="red",marker='o',label='CDF')

for x in range(len(Samples_c0)):
	pyplot.hist(Samples_c0[x], bins=10) 
	pyplot.show()	