#Python program to print even length words in a string

def print_even_length_words(string):
    word=string.split(' ')
    print(word)
    words=[]
    for i in word:
        if len(i)%2 ==0:
            words.append(i)
            
    return " ".join(words)
    
string=  "This is a python language"
print(print_even_length_words(string))