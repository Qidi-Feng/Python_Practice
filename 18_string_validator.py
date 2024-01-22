if __name__ == '__main__':
	s = raw_input()
	print(any(i.isalnum() for i in s))   ##any returns True if ANY item in a iterable is true.
	print(any(i.isalpha() for i in s))
	print(any(i.isdigit() for i in s))
	print(any(i.islower() for i in s))
	print(any(i.isupper() for i in s))
