t = int(input())
a = list(map(int,input().split()))
n = len(a)
x = int(0)
y = int(0)
z = int(0)

for i in range (0,n):
    if (a[i] > 0):
        x = x + 1
    if(a[i] < 0):
        y = y + 1
    if (a[i] == 0):
        z = z + 1
        
print (x/n)
print(y/n)
print(z/n)
