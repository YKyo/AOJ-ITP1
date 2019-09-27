while True:
	I = input()
    x,y = map(int, I.split())
    
    if x == 0 and y == 0:
        break
        
    if x > y:
        x,y = y,x
    print("%d %d" %(x,y))