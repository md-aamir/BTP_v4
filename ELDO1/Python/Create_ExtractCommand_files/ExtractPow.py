file1 = open('Power.cir', 'w') 				
begin=0
end=begin+0.1
i=0
while begin<=33:
	s=".EXTRACT FILE=Power label = pow"+str(i)+" (1.2*integ(I(v0),"+str(begin)+"N,"+str(end)+"N)/0.01N)"+"\n"
	file1.write(s)
	begin=end
	end=begin+0.01
	print(begin," ",end)
	i=i+1
