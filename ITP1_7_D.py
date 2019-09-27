I = input()
n, m, l = map(int, I.split())

A = [[] for j in range(n)]
B = [[] for j in range(m)]
C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
	A[i] = list(map(int, input().split()))
	
for i in range(m):
	B[i] = list(map(int, input().split()))

for i in range(n):
	for j in range(l):
		for k in range(m):
			C[i][j] += A[i][k] * B[k][j]
			
for i in range(n):
	for j in range(l):
		if j!=l-1:
			print(C[i][j], end=" ")
		else:
			print(C[i][j])