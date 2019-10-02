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


dice1 = Dice()
dice2 = Dice()
top, front, right, left, behind, bottom = map(int, input().split())
dice1.setNum(top, front, right, left, behind, bottom)
top, front, right, left, behind, bottom = map(int, input().split())
dice2.setNum(top, front, right, left, behind, bottom)
c = list("ENSW")
k = 1000
flag = False

for i in range(k):
	dice1.roll(random.choice(c))
	if dice1.top==dice2.top and dice1.front==dice2.front and dice1.right==dice2.right and dice1.left==dice2.left and dice1.behind==dice2.behind and dice1.bottom==dice2.bottom:
		flag = True

if flag:
	print("Yes")
else:
	print("No")