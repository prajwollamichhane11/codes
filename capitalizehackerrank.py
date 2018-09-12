def solve(s):
    s = s.split(" ")
    
    for i in range (0,len(s)):
        s[i] = s[i].capitalize()

    s = " ".join(s)        
    
    return s
