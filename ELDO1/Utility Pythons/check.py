file1 = open("Output","r+")
Out=file1.read().split()
res = [sub.replace('*BITS', '') for sub in Out]
res = [sub.replace('=', '') for sub in res]	
while("" in res) : 
    res.remove("") 
print(res)