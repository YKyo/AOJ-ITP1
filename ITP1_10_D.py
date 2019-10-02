import math

n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))

D = [0 for i in range(4)]

for p in range(1,5):
	S = 0
  
	if p==1 or p==2 or p==3: #p=1,2,3の時
		for i in range(n):
			S += (abs(X[i] - Y[i]))**p
		D[p-1] = S**(1/p)
    
	elif p==4:                         #p=無限大の時
		for i in range(n):
			if D[3]<abs(X[i]-Y[i]):
				D[3] = abs(X[i] - Y[i])
				
for i in D:
	print("%.5f" %(i))