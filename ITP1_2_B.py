I = input()
a,b,c = map(int, I.split())

if a < b and b < c:
    print('Yes')
else:
    print('No')