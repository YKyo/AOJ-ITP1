while True:

	I = input()
	InputList = I.split()

	a = int(InputList[0])
	op = InputList[1]
	b = int(InputList[2])

	if op == "?":
		break
		
	if op == "+":
		print("%d" %(a+b))
	elif op == "-":
		print("%d" %(a-b))
	elif op == "*":
		print("%d" %(a*b))
	elif op == "/":
		print("%d" %(a/b))
