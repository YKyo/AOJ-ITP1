I = input()
r, c = map(int, I.split())

table = [[0 for i in range(c+1)] for j in range(r+1)]

for i in range(r):
	InputList = list(map(int, input().split()))
	for j in range(c):
		table[i][j] = InputList[j]
	
for i in range(r):
	for j in range(c):
		table[i][c] += table[i][j]
		table[r][j] += table[i][j]
		table[r][c] += table[i][j]
		
for i in range(r+1):
	for j in range(c+1):
		if j!=c:
			print("%d " %(table[i][j]), end="")
		else:
			print(table[i][j])