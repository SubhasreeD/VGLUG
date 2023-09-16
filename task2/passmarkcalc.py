n=int(input())
marks=[]
a=[]
for i in range(n):
    b=int(input())
    marks.append(b)
for i in marks:
    if i>=35:
        a.append("pass")
    else:
        a.append("fail")
print(*a,sep=",")
