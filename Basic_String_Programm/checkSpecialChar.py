#check if a string contains any special character

def check(string):
    special_characters = "!@#$%^&*()_+=-{}[]|:;<>,.?/~`"
    for char in string:
        if char in special_characters:
            return "Contain special characters: " + char
    return "Contain no special characters: " + char

string = "Geeks For Geeks"

print(check(string))