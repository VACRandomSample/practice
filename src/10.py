k = int(input())
l = int(input())
m = int(input())
n = int(input())
if k == m or l == n or (k + l + m + n) % 2 == 0:
    print("yes")
else: print("no")