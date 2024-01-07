import re
def find_cap(str):
    output=re.findall("^[A-Z]+",str)
    return  output
str=input()
val=find_cap(str)
print(val)
