N = int(raw_input())
M = map(int,raw_input().split())
print(M)
t = tuple(M)
print(t)
result = hash(t)

print(result)
