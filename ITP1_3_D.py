I = input()
a, b, c = map(int, I.split())

counter = 0

for i in range(a, b+1):
	if c%i == 0:
		counter += 1
		
print(counter)