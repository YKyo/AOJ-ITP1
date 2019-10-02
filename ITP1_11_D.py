import random

class Dice():
	def __init__(self):
		self.top = 1
		self.front = 2
		self.right = 3
		self.left = 4
		self.behind = 5
		self.bottom = 6
		
	def setNum(self, top, front, right, left, behind, bottom):
		self.top = top
		self.front = front
		self.right = right
		self.left = left
		self.behind = behind
		self.bottom = bottom
	
	def roll(self, dir):
		if dir=="E":
			self.setNum(self.left, self.front, self.top, self.bottom, self.behind, self.right)
		if dir=="N":
			self.setNum(self.front, self.bottom, self.right, self.left, self.top, self.behind)		
		if dir=="S":
			self.setNum(self.behind, self.top, self.right, self.left, self.bottom, self.front)	
		if dir=="W":
			self.setNum(self.right, self.front, self.bottom, self.top, self.behind, self.left)

c = list("ENSW")
k = 1000
flag = False

n = int(input())
InputList = [[None] for i in range(n)]
for i in range(n):
	InputList[i] = list(map(int, input().split()))

for j in range(n):
	dice1.setNum(InputList[j][0], InputList[j][1], InputList[j][2], InputList[j][3], InputList[j][4], InputList[j][5])
	for k in range(j+1, n):
		dice2.setNum(InputList[k][0], InputList[k][1], InputList[k][2], InputList[k][3], InputList[k][4], InputList[k][5])
		for i in range(k):
			dice1.roll(random.choice(c))
			if dice1.top==dice2.top and dice1.front==dice2.front and dice1.right==dice2.right and dice1.left==dice2.left and dice1.behind==dice2.behind and dice1.bottom==dice2.bottom:
				flag = True

if flag==True:
	print("No")
else:
	print("Yes")