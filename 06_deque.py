from collections import deque
time = int(input())
##learn to use deque object
d = deque()                 
for _ in time:
	operation = input().split()
	if len(operation)==2:

##learn to combine variables and strings
		method = ('d.' + operation[0] + '(' + operation[1] + ')')
	else:
		method = ('d.' + operation[0] + '()')

##learn to execute a command by eval
	eval(method)

##learn to print a list
print(*d)
