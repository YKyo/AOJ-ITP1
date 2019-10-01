n = int(input())
Point_Taro = 0
Point_Hanako = 0

for i in range(n):
	Card_Taro, Card_Hanako = input().split()
	if Card_Taro < Card_Hanako:
		Point_Hanako += 3
	elif Card_Taro > Card_Hanako:
		Point_Taro += 3
	else:
		Point_Taro += 1
		Point_Hanako += 1
		
print("%d %d" %(Point_Taro, Point_Hanako))