def is_symmetrical(s):
    length=len(s)
    mid=length//2
    
    if length%2==0:
        return s[:mid]==s[mid:]
    else:
        return s[:mid]==s[mid+1:] 
    
s='amaama'
if is_symmetrical(s):
    print("The entered string is symmetrical")
else:
    print("The entered string is not symmetrical")