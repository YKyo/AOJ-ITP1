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
top, front, right, left, behind, bottom = map(int, input().split())
dice1.setNum(top, front, right, left, behind, bottom)
q = int(input())
c = list("ENSW")

for i in range(q):
	Top, Front = map(int, input().split())
	while True:
		dice1.roll(random.choice(c))
		if dice1.top==Top and dice1.front==Front:
			print(dice1.right)
			break