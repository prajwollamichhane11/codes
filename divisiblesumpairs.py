n, k = list(map(int,input().split()))
arr = list(map(int,input().split()))
count = 0
for i in range(0, n):
    for j in range(i+1, n):
        if ((arr[i] + arr[j]) % k == 0):
            count += 1
         print (count)   
print (count)
