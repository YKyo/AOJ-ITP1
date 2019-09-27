while True:

	I = input()
	n, x = map(int, I.split())
	
	counter = 0
	
	if n==0 and x==0:
		break
	
	for i in range(1, n+1):
		for j in range(i, n+1):
			for k in range(j, n+1):
				if i!=j and i!=k and j!=k:
					S = i+j+k
					if S==x:
						counter += 1
						
	print(counter)