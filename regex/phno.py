import re
def find_phno(str):
    output=re.findall(r"\+(\d+)\s+(\d+)",str)
    return  output
str=input()
val=find_phno(str)
print(val)
