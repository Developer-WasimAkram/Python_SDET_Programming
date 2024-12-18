# Python | Word location in String

#Method 1: Using re.findall() + index() 

import re

def word_location(string, word):
    string=string.split()

    
    for idx in string:
        if len(re.findall(word, idx)) > 0:
            res=string.index(idx)+1
           
    return res
    
def word_location2(string, word):
    string=string.split() 
    return string.index(word)+1
    
    
    
    
    
    
    
    
    
string='geeksforgeeks is best for best geeks'
word = 'best'
print(f' Using Method 1 location of {word}' ,word_location(string, word))
print(f' Using Method 2 location of {word}', word_location2(string, word))