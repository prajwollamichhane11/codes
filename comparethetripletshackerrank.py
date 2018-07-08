a = list(map(int,input().split()))
b = list(map(int,input().split()))
x = int(0)
y = int(0)
for i in range (0,3):
    if (a[i] > b[i]):
        x = x + 1
    if(a[i] < b[i]):
        y = y + 1
print (x, end= " ",flush = True)
print(y)
