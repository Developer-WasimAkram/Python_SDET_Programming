# Python | Word location in String

#Method 1: Using re.findall() + index() 

import re

def word_location(string, word):
    string=string.split()
 
    
    for idx in string:
        if len(re.findall(word, idx)) > 0:
            res=string.index(idx)+1
           
    return res
    
string='geeksforgeeks is best for geeks'
word = 'best'
print(word_location(string, word))