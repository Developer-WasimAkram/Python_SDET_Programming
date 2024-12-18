
#Method #1: Using loop + join() + split()
def word2num(str):
    dict_word2num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }
    num_list = [dict_word2num[x] for x in str.split()]
    return ''.join(num_list)
str="zero four zero one"



print(word2num(str))