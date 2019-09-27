I = input()
n, m = map(int, I.split())

A = [[0 for i in range(m)] for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]

# Input A
for x in range(n):
	InputList = list(map(int, input().split()))
	for y in range(m):
		A[x-1][y-1] = InputList[y]

# Input b		
for x in range(m):
	InputNum = int(input())
	b[x-1] = InputNum

# Output c
for i in range(n):
	for j in range(m):
		c[i] += A[i-1][j-1]*b[j-1]
	print(c[i])		