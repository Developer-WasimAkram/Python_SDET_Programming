#String slicing in Python to Rotate a String

'''
Given a string of size n, write functions to perform following operations on string.

Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n).

Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe" 
         Right Rotation : "ksGeeksforGee"  
'''

def rotate(str,d):
    Lfirst=str[0:d]
    Lsecond=str[d:]
    
    Rfirst=str[0:len(str)-d]
    Rsecond=str[len(str)-d:]   
    
    left_rotation=Lsecond+Lfirst
    right_rotation=Rsecond+Rfirst
    
    return left_rotation, right_rotation
    
    
s = "GeeksforGeeks"
d = 2
print(rotate(s,d))