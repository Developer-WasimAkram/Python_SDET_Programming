'''
Sometimes, while working with Python Strings, we have problem in which 
we need to perform a case conversion of String. This a very common problem. 
This can have application in many domains such as web development. Lets discuss certain ways in which this task can be performed.

Input : geeks_for_geeks Output : GeeksforGeeks
Input : left_index Output : leftIndex

'''
#Method 1 : Using title() + replace() 

def snake_pascal_title(string):
    return string.replace("_", "").title()
string="geeksforgeeks_is_best"

print(snake_pascal_title(string))


# Method2 Using capwords()
import string
def snake_pascal_capwords(strg):
    res=strg.replace("_", "")
    return string.capwords(res)
strg="geeksforgeeks_is_best"
print(snake_pascal_capwords(strg))

#Method 3 using for loops:
strg="geeksforgeeks_is_best"


def snake_pascal_for(strg):
    res=strg.split("_")
    x=[]
    for i in res:
        x.append(i.title())    
    return "".join(x)

print(snake_pascal_for(strg))
