# Python – Words Frequency in String Shorthands
string = 'Gfg is best' 
Output ={'Gfg': 1, 'is': 1, 'best': 1} 
# Method 1: Using dictionary comprehension + count() + split() 

def wordsFrequnecyInstring1(string):
    return { word: string.count(word) for word in string.split(' ')}
print(wordsFrequnecyInstring1(string))


#Method 2 using Counter method 

from collections import Counter

def wordsFrequnecyInstring2(string):
    return dict(Counter(string.split(' ')))

print(wordsFrequnecyInstring2(string))

#Method 5: Using set() and list comprehension

def wordsFrequnecyInstring3(string):
    return {word: string.count(word) for word in set(string.split(' '))}
print(wordsFrequnecyInstring3(string))

