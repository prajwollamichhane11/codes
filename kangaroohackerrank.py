def kangaroo(x1, v1, x2, v2):
    if((x1>x2 and v1>v2) or (x1<x2 and v1<v2) or (v1-v2)==0):
        return "NO"
    if((x1 - x2) % (v2 - v1)) == 0:
        return "YES"
    else:
        return "NO"
    
x1,v1,x2,v2 = map(int,input().split())

print(kangaroo(x1,v1,x2,v2))
