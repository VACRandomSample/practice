a = int(input())
b = int(input())
c = int(input())

m = int(input())
k = int(input())

mk = m * k
if a * b == mk:
    print("ab")
elif a * c == mk:
    print("ac")
elif b * c == mk:
    print("bc")