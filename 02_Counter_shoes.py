from collections import Counter            ## a new function Counter
X = int(raw_input())                       ##use raw_input()
counts = Counter(raw_input().split())      ##use .split() to split by space
N= int(raw_input())                        ##python receive string a default, if you want it to be a number, use int
ans=0

for _ in range(N):                         ## use _ in for if there is no use for it in the further steps.
	shoe_size, amount = raw_input().split()   
	if counts[shoe_size]:              ##check if a key exists in a dic
		ans += int(amount)
		counts[shoe_size] -= 1

print(ans)
