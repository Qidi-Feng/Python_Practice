from collections import OrderedDict                   ##learn to use OrderedDict

num = int(raw_input())

od = OrderedDict()                                    ##define a OrderedDict

for _ in range(num):
	word = raw_input()
	if word in od:
		od.update({word:od.get(word)+1})	##use .update function and .get function
	else:
		od.update({word:1})
print(len(od))
print(od.values())				        ##use .values function in dict
