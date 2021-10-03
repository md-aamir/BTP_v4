file2 = open("Output","r+")
Out=file2.read().split()
Out=Out[10:]
enc_text=[]
t=[]
for i in range(4):
    for j in range(128):
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
for x in range(len(enc_text)):
    enc_text[x].reverse()
    enc_text[x]="".join(enc_text[x])
for i in range(len(enc_text)):
    enc_text[i]=int(enc_text[i],2)
print(enc_text)
#1. List reversal
#2. Extract value to dec
#3. Test :)
