
string="geeks for geeks"
substring="geeks"

#Method 1 if else:
def string_substring_Check1( string,substring):
    if substring in string:
        return True
    else:
        return False
    
print(string_substring_Check1( string,substring))


#Method 2 using find:
def string_substring_Check2(string,substring):
    if string.find(substring) != -1:
        return True
    else:
        return False
    

print(string_substring_Check2(string,substring))

#Method 3 using string.count
def string_substring_Check3(string,substring):
    if string.count(substring) >0:
        return True
    else:
        return False
print(string_substring_Check3(string,substring))