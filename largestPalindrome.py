# Largest Palindrome from the multiple of 3 character numbers

def isPalindrome(value):
	value = str(value)
	if value == value[::-1]:
		return 1
	else:
		return 0


def genratePalindrome():
	chkPnts = [999,899,799,699,599,499,399,299,199,99]
	maxm = 0
	for i in range(len(chkPnts)):
		for j in range(chkPnts[i],chkPnts[i+1],-1):
			for k in range(chkPnts[i],chkPnts[i+1],-1):
				val = j * k
				if isPalindrome(val) == 1:
					maxm = val

					break
			if isPalindrome(val) == 1:
					maxm = val

					break
		if isPalindrome(val) == 1:
					maxm = val
					break
	return maxm
print(genratePalindrome())