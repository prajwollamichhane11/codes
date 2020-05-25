#n is the total nummber of contests
#k is the amount of contests Lena can loose
n,k = map(int, input().split())
L = []
T = []
for i in range(n):
	a,b = map(int, input().split())
	L.append(a)
	T.append(b)
L,T = zip(*sorted(zip(L,T)))

luckSum = L.sum()

count = 0
for i in range(n):
	if count != k:
		if T[i] == 1:
			luckSum -= L[i]
			count += 1
		else:
			continue

	else:
		break

print(luckSum)