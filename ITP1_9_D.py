str = input()
q = int(input())

for i in range(q):
	InputList = input().split()
	command = InputList[0]
	a = int(InputList[1])
	b = int(InputList[2]) + 1
	
	if command=="print":
		print(str[a:b])
	elif command=="reverse":
		str = str[:a] + str[a:b][::-1] + str[b:]
	elif command=="replace":
		p = InputList[3]
		str = str[:a] + p + str[b:]