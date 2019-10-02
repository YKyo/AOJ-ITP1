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
command = list(input())

for i in command:
	dice1.roll(i)
	
print(dice1.top)