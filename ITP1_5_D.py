n = int(input())

for i in range(n):
	i += 1
	# "x" in "xyz" : "xyz"に"x"が含まれていればtrue
	if i%3 == 0 or "3" in str(i):
		print(" ", i, end="")