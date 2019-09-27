while True:

	I = input()
	m, f, r = map(int, I.split())
	
	if m==-1 and f==-1 and r==-1:
		break
		
	if m==-1 or f==-1 or m+f<30:
		print("F")
	elif 30<=m+f and m+f<50:
		if 50<=r:
			print("C")
		else:
			print("D")
	elif 50<=m+f and m+f<65:
		print("C")
	elif 65<=m+f and m+f<80:
		print("B")
	else:
		print("A")