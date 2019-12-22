a, b = map(int, input().split())

if abs(a-b)%2 == 0:
    print(int((a+b)/2))
else:
    print('IMPOSSIBLE')
