#Python – Least Frequent Character in String


#Metho 1

def leastFrequncyChar(string):
    char_count={}
    for char in string:
        if char in char_count:
           char_count[char]+=1
        else:
           char_count[char]=1
           
    return min(char_count,key=char_count.get)
    
string='abbcccddddeeeee'  
print(leastFrequncyChar(string))


#Method 2  Using Counter

from collections import Counter

def leastFrequncyChar_Counter(string):
    char_count = Counter(string)
    return char_count.most_common()[-1][0]

print(leastFrequncyChar_Counter(string))