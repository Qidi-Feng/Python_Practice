##One solution:
def swap_case(s):
	j = ""   ##you have to define another variable for the result. You cannot change a string directly.
	for i in range(len(s)):
		if s[i].isupper():
			j += s[i].islower()
		elif s[i].islower():
			j += s[i].isupper()
		else:
			j += s[i]
	return j
if __name__ == '__main__':
	s = input()
	result = swap_case(s)
	print(result)

##Second solution:
def swap_case(s):
	j = s.swapcase(s)
	return j

if __name__ == '__main__':
	s = input()
	result = swap_case(s)
	print(result)
