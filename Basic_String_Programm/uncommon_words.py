#Python program to find uncommon words from two Strings

'''
Given two sentences as strings A and B. The task is to return a list of all uncommon words. A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence. Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters. 

Examples:
Input : A = “Geeks for Geeks”,  B = “Learning from Geeks for Geeks”
Output : [‘Learning’, ‘from’]
Input : A = “apple banana mango” , B = “banana fruits mango”
Output : [‘apple’, ‘fruits’]
'''


def uncommon_words(str1,str2):
    str1 = str1.split()
    str2 = str2.split()
    
    dict={}
    dict2={}
    
    for word in str1:
        dict[word] = dict.get(word,0)+1
    for word in str2:
        dict[word] = dict.get(word,0)+1
        
    return [ word  for word in dict if dict[word]==1]


#Method 2 

def uncommon_words1(str1,str2):
    str1 = str1.split()
    str2 = str2.split()
    uncommon_words = []
    
    for word in str1:
        if word not in str2:
            uncommon_words.append(word) 
            
    for word in str2:
        if word not in str1:
            uncommon_words.append(word)          
    return uncommon_words
    
    
    
    
    
    
    
    
    
 
 
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"   
print(uncommon_words(A,B))
print(uncommon_words1(A,B))