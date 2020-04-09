n = int(input())
nums = list(map(int,input().split()))


minm = 1000000000000000
nums.sort()
for i in range(n-1):
    diff = nums[i]-nums[i+1]
    absDiff = abs(diff)

    if absDiff < minm:
        minm = absDiff
print(minm)
