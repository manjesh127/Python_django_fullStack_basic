arraycheck = ([1,2,3,1,2,3,1])

def array_check(num):
    
    for i in range(len(num)-2):
        if num[i]==1 and num[i]==2 and num[i]==3:
            return True
    return False        

array_check(arraycheck) 