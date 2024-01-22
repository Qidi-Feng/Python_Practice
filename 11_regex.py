import re
n = int(input())

pattern1 = r'(?<=\s)&&(?=\s)'
pattern2 = r'(?<=\s)\|\|(?=\s)'

repl1 = 'and'
repl2 = 'or'

for _ in range(n):
	string = input()
	print(re.sub(pattern1, repl2, re.sub(pattern2, repl2, string)))
