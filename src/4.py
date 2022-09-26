n = int(input())

f1 = f2 = 1

while n-2 > 0:
    f1, f2 = f2, f2+f1
    n -= 1
print(f2)