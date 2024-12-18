#Python | Check if a given string is binary string or not

'''Input: str = "01010101010"
Output: Yes

Input: str = "geeks101"
Output: No
'''
#Method 1 using set.
def binary_string(str):
    string=set(str) 
    binary={'0','1'}
    
    if string == binary or string == '0' or string == '1' :
        print(('Given string is binary string ') + str)
    else:
        print(('Given string is not binary string ') + str)   
        
str = "01010101010"  
#str='asbdhbf'   
print(binary_string(str))

#Method 2 using iteration

def binary_string2(str):
    
    for char in str:
        if char not in '01':
            return False
        else:
            return True
            
print(binary_string2(str))
    
    
    

