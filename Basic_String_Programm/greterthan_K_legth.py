#Find words which are greater than given length k


def string_k(k,string):
    s=[]
    string=string.split()
    for word in string:
        if len(word) >k:
            s.append(word)
    return ' '.join(s)

k=4 
string="hello geeks for geeks  is computer science portal" 
print(string_k(k,string))