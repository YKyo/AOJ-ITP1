n = int(input())

I = input()
InputList = list(map(int, I.split()))

minnum = InputList[0]
maxnum = InputList[0]
total = 0

for i in InputList:
	if minnum > i:
		minnum = i
	if maxnum < i:
		maxnum = i
	total += i
	
print("%d %d %d" %(minnum, maxnum, total))