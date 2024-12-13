

def revereString(s:str) ->str:
    length=len(s)
    reversed_s=''
    
    for i in s:
        reversed_s=i+reversed_s
        
    return reversed_s


print(revereString('wasim'))