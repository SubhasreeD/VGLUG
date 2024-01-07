import re
def remove_int(str):
    output=re.sub("[0-9]","",str)
    return  output
str=input()
val=remove_int(str)
print(val)
