while True:
	
	I = input()
	
	if I=="-":
		break
	
	m = int(input())
	
	for i in range(m):
		h = int(input())
		I = I[h:] + I[:h]	#[:h]で先頭からh字、[h:]でh+1字から末尾まで切り取り
	
	print(I)