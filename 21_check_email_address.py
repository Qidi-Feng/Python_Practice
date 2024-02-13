import re
def email_address(address):
	pattern = r'[a-zA-Z][a-zA-Z0-9\-\.\_]*\@[a-zA-Z]+\.[a-zA-Z]{1,3}'   ##[a-zA-Z]{1,3} means there are 1,2 or 3 alphabetic characters.
	if re.findall(pattern,address):
		return 'YES'
	else:
		return 'NO'
times = int(raw_input())
for i in range(0,times):
	entry = raw_input()
	name, address = entry.split()
	answer = email_address(address)
	print(answer)
	if answer == 'YES':
		print(entry)
	else:
		next


##alternative: use re.fullmatch
re.findall: Return all non-overlapping matches of pattern in string, as a list of strings or tuples. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.
