while True:

	I = input()
	H, W = map(int, I.split())
	
	if H==0 and W == 0:
		break

	for i in range(H):
		for j in range(W):
			print("#", end="")
		print()