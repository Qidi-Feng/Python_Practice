##lists are mutable, string and tuples are immutable (cannot be changed)

def mutate_string(string, position, character):
	my_str = string[:position] + character + string[(position+1):]
	return my_str

if __name == '__main__'
	s=input()
	i, c = input().split()
	s_new = mutate_string(s, i, c)
	print(s_new)
