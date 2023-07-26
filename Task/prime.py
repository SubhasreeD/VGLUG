x=int(input())
y= int(input())
for i in range(x,y):
	count = 2
	while(i%count!=0):
		count+=1
	if(count == i):
		print("prime")
	else:
		print("not a prime")

