while True:
	
	I = input()
	
	if I=="0":
		break
	
	x = list(map(int, list(I)))
	
	print(sum(x))