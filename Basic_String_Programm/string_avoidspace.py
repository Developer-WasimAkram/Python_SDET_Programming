#Avoid Spaces in string length

#Method #1 : Using isspace() + sum()

def avoidSpace1(string):
    count=0 
    for char in string:
        if char.isspace():
            count+=1
            
    return len(string)-count



# Avoid Spaces in Characters Frequency
# Method 2Using sum() + len() + map() + split()

def avoidSpace2(string):
    res=sum(map(len,string.split()))
    return res

# Method 3 Using replace() 

def avoidSpace3(string):
    string=string.replace(" ", "")
    return len(string)

#Method 4 usning join()
def avoidSpace4(string):
   res = len(''.join([char for char in string if char != ' ']))
   return res

s='geeksforgeeks 33 is   best'

print("The Characters Frequency avoiding spaces by avoidSpace1 : ",+avoidSpace1(s))
print("The Characters Frequency avoiding spaces by avoidSpace2 : ",+avoidSpace2(s))
print("The Characters Frequency avoiding spaces by avoidSpace3 : ",+avoidSpace3(s))
print("The Characters Frequency avoiding spaces by avoidSpace4 : ",+avoidSpace4(s))

