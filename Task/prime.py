x=int(input())
y= int(input())
if(x>1):
	for i in range(x,y+1):
		count = 2
		while(i%count!=0):
			count+=1
		if(count == i):
			print(i,"is a prime number")
		else:
			print(i,"is not prime a number")

