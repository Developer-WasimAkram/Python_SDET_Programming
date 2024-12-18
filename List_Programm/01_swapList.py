#Python program to interchange first and last elements in a list

def interchange_first_last(lst):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst





lst = [0,1,2,3,4,5,6,7,8,9,10,11,12]
print(interchange_first_last(lst))