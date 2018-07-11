n = int(input())
t = int(input())
trr = list(map(int,input().split())) 
count = 0

for i in range(0,len(trr)):
    count = count + 1
    if(trr[i] == n):
        break
        
print(count-1)
