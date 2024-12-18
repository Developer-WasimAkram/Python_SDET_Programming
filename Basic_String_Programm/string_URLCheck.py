#Python | Check for URL in a String
'''
we will need to accept a string and we need to check if the string contains any URL in it. If the URL is present in the string, we will say URL’s been found or not and print the respective URL present in the string. We will use the concept of Regular Expression of Python to solve the problem.

'''
import re
def checkURL_string(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url=re.findall(regex,string)
    
    return [x[0] for x in url]


string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
print("Urls: ",checkURL_string(string))