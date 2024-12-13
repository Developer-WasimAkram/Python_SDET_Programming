
#Remove Letters From a String in Python


def remove_letters_listcomp(string, letters):
    result= ''.join([c for c in string if c != letters])
    return result

print(remove_letters_listcomp("wasimm", 'm'))


def remove_letters(string, letters):
    result=''
    
    for c in string:
        if c != letters:
            result+=c
            
    return result
print(remove_letters("Awesome", 'o'))



def remove_letters_filter(string, letters):
    return ''.join(filter(lambda x: x != letters,string))

print(remove_letters_filter("WOW MOMO", 'O'))


# Method 4  slicing

    
def remove_letters_slicing(s, letters):
    idx=s.find(letters)
    if idx != -1:
        string=s[:idx] + s[idx+1:]
        return s
    
    
print(remove_letters_slicing('hello world', "o"))