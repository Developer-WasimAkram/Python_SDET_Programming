#Remove All Duplicates from a Given String in Python


# Method 1: Using a list to store unique words and joining them at the end
def remove_duplicates(string):
    string=string.split()
    result=[]
    for char in string:
        if char not in result:
            result.append(char)       
    return ''.join(result)
    
string="geeks for geeks"
print(remove_duplicates(string))
# Method 1: Using a list to store unique char and joining them at the end
def remove_duplicates1(string):
    string=set(string)
    result=[]
    for char in string:
        if char not in result:
            result.append(char)       
    return ''.join(result)
    
string1="geeksforgeeks"
print(remove_duplicates1(string1))