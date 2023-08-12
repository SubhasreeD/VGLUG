#pass by reference
def fun(list):
	list.append("c")
list=["a","b"]
fun(list)
print(list)


#pass by value
def val(value):
	value=1
value=10
val(value)
print (value)





