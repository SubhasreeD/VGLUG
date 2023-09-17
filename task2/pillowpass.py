tot_persons=int(input())
time=int(input())
dir=1
person=1
for i in range(time):
	if person==1 and dir==-1:
		dir=1
	elif person==tot_persons and dir==1:
		dir=-1
	if dir==1:
		person+=1
	elif dir==-1:
		person-=1
print("time:" ,time,"pillow held by person:",person)
