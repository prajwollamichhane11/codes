t = list(map(int,input().split()))
v = list(map(int,input().split()))
x = int(input())

s = sum(v) - v[t[1]]
s = s//2

if(s == x):
    print("Bon Appetit")
else:
    print(x-s)

