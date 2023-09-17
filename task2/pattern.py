n=6
start='A'
space=" "
for i in range(0,n):
	print(" "*(n-i),end=" ")
	for j in range(0,i+1):
		print(chr(ord(start)+j),end="") 
	for j in range(i-1,-1,-1):
		print(chr(ord(start)+j),end="")
	print("\n")

