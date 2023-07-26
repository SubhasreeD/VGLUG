str1=input()
str2=input()
if(len(str1)==len(str2)):
	if(sorted(str1)==sorted(str2)):
		print("given string is anagram")
	else:
		print("given string is not an anagram")
