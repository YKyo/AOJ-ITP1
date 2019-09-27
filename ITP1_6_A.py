n = int(input())

I = input()
InputList = list(map(int, I.split()))

for i in range(n, 0, -1):
	if i!=0:
		print(InputList[i-1], end=" ")
	elif i==0:
		print(InputList[i-1])