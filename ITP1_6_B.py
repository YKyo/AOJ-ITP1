cards = [[False for i in range(13)] for j in range(4)]

pattern = ["S", "H", "C", "D"]

n = int(input())

# Input
for x in range(n):
	I = input().split()
	ch = I[0]
	rank = int(I[1])
	cards[pattern.index(ch)][rank-1] = True	
	
# Output
for i in range(0, 4):
	for j in range(0, 12):
		if cards[i][j]==False:
			print(pattern[i], j+1)	