from collections import deque
d = deque()
for i in range(int(raw_input())):
	c = raw_input().split()

##learn to use getattr for an object
	method = getattr(d, c[0])
	if len(c) == 2:

##learn to execute this object
		method(c[1])
	else:
		method()
print(" ".join(d))
