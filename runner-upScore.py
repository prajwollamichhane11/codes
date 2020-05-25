n =  int(input())
A = list(map(int,input().split()))

# A = set(sorted(A))
A.sort()

for i in range(n):
    if A[-i-1] != A[-i-2]:
        print(A[-i-2])
        break