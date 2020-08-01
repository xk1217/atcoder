x = int(input())
a = 100
i = 1
while(1):
    a = int(a + 0.01*a)
    if (a>=x):
        print(i)    
        break
    i +=1

    
