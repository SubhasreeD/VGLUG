import re
def remove_space(str):
    output=re.sub("\s+"," ",str)
    return  output
str=input()
val=remove_space(str)
print(val)
