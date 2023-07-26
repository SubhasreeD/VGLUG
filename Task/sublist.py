l1=[[1,2,3],[2,30,2],[3,4,5]]
max=0
c=0
for i in l1:
	isum=sum(i)
	if(isum>max):
		max=isum
		c=i
print(c)
print(l1.index(c))
	
