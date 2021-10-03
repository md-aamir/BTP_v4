file2 = open("Output","r+")
Out=file2.read().split()
Out=Out[10:]
enc_text=[]
t=[]
i=3
for j in range(64,96):
        s="*BITS"+str(i)+str(j)
        m=Out.index(s)
        temp=float(Out[m+2])
        if(temp>0.5):
            temp0="1"
        else:
            temp0="0"
        t.append(temp0)
        if(j%32==31):
            enc_text.append(t)
            t=[]
enc_text[0].reverse()
x=0
enc_text[x]="".join(enc_text[x])
print(int(enc_text[0],2))
