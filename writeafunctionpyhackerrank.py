def is_leap(year):
    
    if(year != 2100 or year != 2200 or year != 2300):
        if (year % 4 == 0):
            return True
        else:
            return False
    else:
        return False
       
year = int(input())
print(is_leap(year))       
