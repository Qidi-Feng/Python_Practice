def count_substring(string, sub_string):
	count = 0
	for i in range(0, len(string)):
		if (len(string) - i) < len(sub_string):
			next
		else:
			test_string = string[i:(i+len(sub_string))]  ##string[0:3] means index 0,1,2
			if test_string == sub_string:
				count += 1
	return count

if __name__ == '__main__':
	string = raw_input().strip()
	sub_string = raw_input().strip()
	count = count_substring(string, sub_string)
	print(count)
