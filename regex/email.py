import re
def find_email(str):
    output=re.findall(r"^[a-zA-Z0-9][_a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-z]{2,}",str)
    return  output
str=input()
val=find_email(str)
print(val)
