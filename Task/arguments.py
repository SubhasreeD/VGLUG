#default arg eg
print("default argument ")
def add(x,y=10):
	print(x+y)
add(4)

#keyword arg
print("keyword argument ")
def add(x,y=10):
	print(x+y)
add(x=7)

#positionl arg
print("positionl argument ")
def s(name,age):
	print("my name is",name,"age",age)
s("subha",20)

#arbitary arguments
# 1. *args
print(" *args ")
def fun(*args):
	for i in args:
		print(i)
fun(1,2,3,"str","values")


# 2. **kwargs
print(" **kwargs ")
def fun(**kwargs):
	for key,value in kwargs.items():
		print(key,value)
fun(name="subha",age=20,phno=123)
#TASK
# pass by value,pass by reference


