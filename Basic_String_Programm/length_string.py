#Find Length of String in Python

#Method 1 using len function

def length_string(string):
    return len(string)
s='Hello World'
print("Method_1: Length of string is ",length_string(s))

#Method 2 using for loop

def string_length_count(string):
    count=0 
    for s in string:
        count+=1
    return count

print("Method_2: Length of string using count  is ",string_length_count(s))


#Method 3 using str.count()

def string_length_inbuilt_count(string):
    return string.count("") -1
    
print("Method_3: Length of string using inbuilt count  is ",string_length_inbuilt_count(s))