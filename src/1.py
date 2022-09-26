N = int(input())

arr_ = [ i+1 for i in range(N+1) ]
print(f"{arr_}/n")

for i in range(3, N + 1, 2):
    k = 0
    q = int(N ** 0.5) + 2
    for j in arr_:
        if j > q:
            break
        if i % j == 0:
            k = 1
            break
    if k == 0:
        arr_.append(i)
print(*arr_)
