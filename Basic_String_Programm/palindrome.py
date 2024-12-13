def is_palindrome(num:str) ->str:
    return num==num[::-1]
num='amaama'
if is_palindrome(num):
    print("The entered string is palindrome")
else:
    print("The entered string is not palindrome")