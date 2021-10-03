file1 = open("Output","r+")
Out=file1.read().split()
res = [sub.replace('*BITS', '') for sub in Out]
res = [sub.replace('=', '') for sub in res]	
while("" in res) : 
    res.remove("") 
print(res)
Out=[]
for x in res:
	if(float(x) < 0.8):
		Out.append(0)
	else:
		Out.append(1)
print(Out)