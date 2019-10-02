import math

a, b, C = map(int, input().split())
C = math.radians(C)

#余弦定理
c = (a**2 + b**2 - 2*a*b*math.cos(C))**0.5

#ヘロンの公式
s = (a + b + c) / 2
S = (s*(s-a)*(s-b)*(s-c))**0.5

#高さ
h = 2*S / a

print("%.4f" %(S))
print("%.4f" %(a+b+c))
print("%.4f" %(h))