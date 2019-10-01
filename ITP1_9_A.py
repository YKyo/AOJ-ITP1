W = input()
T = []
counter = 0	

while True:
	InputList = input()
	if InputList=="END_OF_TEXT":
		break
	T += InputList.split()
	
for i in T:
	if i in W and W in i:
		counter += 1
		
print(counter)