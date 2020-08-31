n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

k = []

for i in range(n):
    k.append(abs(t-h[i]*0.006-a))

print(k.index(min(k))+1)