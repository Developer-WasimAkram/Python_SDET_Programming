
#Python Program to Accept the Strings Which Contains all Vowels
'''Firstly, create set of vowels using set() function. 
Check for each character of the string is vowel or not, 
if vowel then add into the set s. After coming out of the loop, 
check length of the set s, 
if length of set s is equal to the length of the vowels set then string is accepted otherwise not. 
'''

#Method 1
def check(string):
    string = string.lower()
    vowels = set('aeiou')
    s = set()
    
    for char in string:
        if char in vowels:
            s.add(char)
        else:
            pass
        
    if len(s) == len(vowels):
        print ('Accepted')
    else:
        print ('Not accepted')
        
        
def check2(string):
    string=string.replace(' ','')
    string=string.lower()
    vowels=[string.count('a'),string.count('e'),string.count('i'),string.count('o'),string.count('u')]
    if vowels.count(0) > 0:
        print('Not accepted')
        print(vowels.count(0))
    else:
        print('Accepted')
        print(vowels.count(0))
        
    
string='ABeeIghiObhkUul'   
print(check(string))        
print(check2(string))