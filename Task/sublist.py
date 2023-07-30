l1=[[2,30,2],[1,2,3],[3,4,5]]
max=0
c=0
a=0
mini=sum(l1[0])
for i in l1:
	isum=sum(i)
	if(isum>max):
		max=isum
		c=i
for j in l1:
	isum=sum(j)
	if(mini>isum):
		mini=isum
		a=j	
print("low value sublist",l1.index(a))
print("low value sublist",l1.index(c))
	
