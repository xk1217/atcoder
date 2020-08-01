n, m = map(int,input().split())
A = list(map(int,input().split()))

cnt = sum(x >= sum(A)/(4*m) for x in A)

if(cnt >= m):
    print('Yes')
   print('No')