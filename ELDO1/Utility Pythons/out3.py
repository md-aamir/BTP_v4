file1 = open("memory_initialization","r+")
pr=[]
Out=file1.read().split()
while(".ic" in Out):
    Out.remove(".ic")
for i in range(4):
    for j in range(128):
        s="v(mem"+str(i)+"_"+str(j)+")="
        Out.remove(s)
for x in Out:
	if(x=="1.2v"):
		pr.append(1)
	else:
		pr.append(0)
print("INPUT")
m=""
for x in pr:
    print(x,end="")
    m=m+str(x)


file2 = open("Output","r+")
Out=file2.read().split()
res = [sub.replace('*BITS', '') for sub in Out]
res = [sub.replace('=', '') for sub in res]	
while("" in res): 
    res.remove("")  
Out=[]
for x in res:
	if(float(x) < 0.8):
		Out.append(0)
	else:
		Out.append(1)
print("\n")
print("Output")

n=""
for x in Out:
    print(x,end="")
    n=n+str(x)
print("\n")
print(n==m)
print("\n")
print(Out==pr)

###############################################INPUT#########################################
y=""
List=[]
for i in range(16):
    y=''.join(map(str, pr[i*32:(i+1)*32-1]))
    List.append(y)

for i in range(len(List)):
    List[i]=int(List[i],2)

print(List)
###############################################INPUT#########################################
#LSB to MSB

def rotate(v, c):
    return ((v << c) & 0xffffffff) | v >> (32 - c)

def quarter_round(x, a, b, c, d):
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 16)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 12)
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 8)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 7)
quarter_round(List, 0, 4,  8, 12)
quarter_round(List, 1, 5,  9, 13)
quarter_round(List, 2, 6, 10, 14)
quarter_round(List, 3, 7, 11, 15)
print(List)

###############################################Output#########################################
y=""
List_out=[]
for i in range(16):
    y=''.join(map(str, Out[i*32:(i+1)*32-1]))
    List_out.append(y)

for i in range(len(List_out)):
    List_out[i]=int(List_out[i],2)

print(List_out)
###############################################Output#########################################