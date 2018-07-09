n = int(input())

arr = list(map(int,input().split()))
max1 = max(arr)
count = 0

for i in range(0,len(arr)):
    if arr[i]==max1:
        count+=1

print(count)
