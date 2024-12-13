#Find Length of String in Python

#Method 1 using len function

def length_string(string):
    return len(string)
s='Hello World'
print("Method_1: Legth of string is ",length_string(s))

#Method 2 using count

def string_length_count(string):
    count=0 
    for s in string:
        count+=1
    return count

print("Method_w: Legth of string using count  is ",string_length_count(s))