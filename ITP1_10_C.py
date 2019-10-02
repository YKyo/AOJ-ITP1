while True:

	n = int(input())
	
	if n==0:
		break

	Scores = list(map(int, input().split()))
	S = 0
	SS = 0
	
	for i in Scores: #平均値
		S += i
	m = S/n
		
	for i in Scores: #分散
		SS += (i - m)**2
	A = SS/n
	
	print("%.4f" %(A**0.5))