def valid_anagram(str1, str2):
	list1 = list(str1)
	list2 = list(str2)
	list1.sort()
	list2.sort()
	print(list1, list2)
	if list1 == list2:
		return True




s = "anagram"
t = "nagaram"

print(valid_anagram(s, t))