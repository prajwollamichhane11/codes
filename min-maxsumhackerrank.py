arr = list(map(int,input().split()))

print(sum(arr)-max(arr),end=" ",flush=True)
print(sum(arr)-min(arr))
