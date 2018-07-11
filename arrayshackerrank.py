n = int(input())
arr = list(map(int,input().split()))
i = 0
c = 0
while(True):
    i = i-1
    print(arr[i],end=" ")
    c = c + 1
    if(c == len(arr)):
        break
