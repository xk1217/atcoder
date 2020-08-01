k = int(input())
a, b = map(int, input().split())

A = a//k
B = b//k

if k == 1:
    print("OK")
elif (B - A)>=1:
    print("OK")
else:
    print("NG")


