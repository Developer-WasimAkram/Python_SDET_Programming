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
    
string='bbcccddddeeeee'  
print(leastFrequncyChar(string))