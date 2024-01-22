def split_and_join(line):
	x = line.split(" ")
	y = tuple(x)   ##join function cannot be applied to list, it can be applied to tuple and dictionary
	z = "-".join(y)
	return z

if __name == '__main__':
	line = input()
	result = split_and_join(line)
	print(result)

Alternative methods:
def split_and_join(line):
	return line.strip().replace(" ", "-")
}
if __name == "__main__":
	line=input()
	result = split_and_join(line)
	print(result)

