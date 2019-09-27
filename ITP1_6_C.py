counter = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())

# Input
for x in range(n):
	I = input()
	b, f, r, v = map(int, I.split())
	counter[b-1][f-1][r-1] += v

# Output
for i in range(4):
	for j in range(3):
		for k in range(10):
			print(" ", counter[i][j][k], end="")
		print()
	if i!=3:
		for k in range(20):
			print("#", end="")
		print()