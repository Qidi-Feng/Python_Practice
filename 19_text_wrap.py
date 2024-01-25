def wrap(string, max_width):
	res = ""
	for i in range(0, len(string)):
		if (i+1)%max_width == 0:
			res += string[i]
			res += "\n"
		else:
			res += string[i]
	return res

if __name__ == '__main__':
	string, max_width = raw_input(), int(raw_input())
	result = wrap(string, max_width)
	print(result)
