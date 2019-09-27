I = input()
a, b = map(int, I.split())

# %x.yf は整数部分x桁、少数部分y桁の出力
print("%d %d %.5f" %(a/b, a%b, a/b))