I = input()
a, b = map(int, I.split())
if a < b:
	print("a < b")
elif a > b:
	print("a > b")
else:
	print("a == b")