I = input()

alphabet = list("abcdefghijklmnopqrstuvwxyz")

for i in alphabet:
	counter = I.count(i)
	print("%s : %d" %(i, counter))