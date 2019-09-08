I = input()
W,H,x,y,r = map(int, I.split())

if r <= x and x <= W-r and r <= y and y <= H-r:
    print('Yes')
else:
    print('No')